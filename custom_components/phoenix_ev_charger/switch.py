import logging
try:
    from homeassistant.components.switch import SwitchEntity
except ImportError:
    from homeassistant.components.switch import SwitchDevice as SwitchEntity

from homeassistant.const import STATE_ON, STATE_OFF
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (CONF_HOST, CONF_PORT,
                                 CONF_SCAN_INTERVAL)
from . import PhoenixEvDevice
from pymodbus.client import ModbusTcpClient
from .const import ATTR_MANUFACTURER, DEVICE_STATUSSES, DOMAIN, SWITCHES, DIGITAL_STATUS

_LOGGER = logging.getLogger(__name__)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Phoenix ev Sensor setup platform."""
    _LOGGER.debug("Phoenix ev charger Switch component running ...")
    if discovery_info is None:
        _LOGGER.error("No Sensor(s) discovered")
        return
    host = ConfigEntry.data[CONF_HOST]
    port = ConfigEntry.data[CONF_PORT]
    devices = []
    for sw in SWITCHES:
        devices.append(
            PhoenixEVSwitch(
                SWITCHES[sw][0], SWITCHES[sw][1], host, port
            )
        )
        _LOGGER.debug("Adding device: %s", SWITCHES[sw][0])
    async_add_entities(devices)


class PhoenixEVSwitch(PhoenixEvDevice, SwitchEntity):
    """Representation of Switch Sensor."""

    # pylint: disable=too-many-instance-attributes

    def __init__(self, name, icon, host, port):
        """Initialize the sensor."""
        self._pre = "sw_"
        self._name = name
        self._host = host
        self._port = port
        self._state = False
        self._icon = icon
        self._data = None
        self._available = 0

    @property
    def is_on(self):
        """Return is_on status."""
        return self._state

    async def async_turn_on(self):
        """Turn On method."""
        client = ModbusTcpClient(host=self._host, port=self._data, timeout=5)
        client.connect()
        _LOGGER.error(
            "Sending ON request to SWITCH device %s (%s)", self._name
        )
        client.write_coil(address=400,value=True)
        self._state = STATE_ON
        client.close()
        self.schedule_update_ha_state()

    async def async_turn_off(self):
        """Turn Off method."""
        client = ModbusTcpClient(host=self._host, port=self._data, timeout=5)
        client.connect()
        _LOGGER.error(
            "Sending OFF request to SWITCH device %s (%s)",  self._name
        )
        client.write_coil(address=400,value=False)
        self._state = STATE_OFF
        client.close()
        self.schedule_update_ha_state()

    @property
    def should_poll(self):
        """No polling needed."""
        return False

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def icon(self):
        """Return the image of the sensor."""
        return self._icon

    @property
    def available(self):
        """Return availability."""
        _LOGGER.debug("Device %s - availability: %s", self._name, self._available)
        return True if self._available == 1 else False

    async def async_update(self):
        """Return sensor state."""
        self._data = self.hass.data[DOMAIN]["data"]
        _LOGGER.debug("REFRESHING SWITCH %s - %s", self._name)
        self._available = 0
        client = ModbusTcpClient(host=self._host, port=self._data, timeout=5)
        client.connect()
        if client.connected:
            self._available = 1
            chargestate_data = client.read_coils(address=400, count=1, slave=0)
            charging = chargestate_data.bits[0]
            if charging:
                self._state = STATE_ON
            else:
                self._state = STATE_OFF
            _LOGGER.debug(self._state)
            client.close()
            return self._state
        return False
