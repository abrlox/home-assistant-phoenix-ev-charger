import logging
try:
    from homeassistant.components.switch import SwitchEntity
except ImportError:
    from homeassistant.components.switch import SwitchDevice as SwitchEntity

from homeassistant.const import CONF_NAME
# STATE_ON, STATE_OFF,
STATE_ON = True
STATE_OFF = False

from . import PhoenixEvDevice
from pymodbus.client import ModbusTcpClient
from .const import ATTR_MANUFACTURER, DEVICE_STATUSSES, DOMAIN, SWITCHES, DIGITAL_STATUS

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    """Phoenix ev Sensor setup platform."""
    hub_name = entry.data[CONF_NAME]
    hub = hass.data[DOMAIN][hub_name]["hub"]

    _LOGGER.debug("Phoenix ev charger Switch component running ...")
    devices = []
    for sw in SWITCHES:
        devices.append(
            PhoenixEVSwitch(
                SWITCHES[sw][0], SWITCHES[sw][1], hub
            )
        )
        _LOGGER.debug("Adding device: %s", SWITCHES[sw][0])
    async_add_entities(devices)


class PhoenixEVSwitch(PhoenixEvDevice, SwitchEntity):
    """Representation of Switch Sensor."""

    # pylint: disable=too-many-instance-attributes

    def __init__(self, name, icon, hub):
        """Initialize the sensor."""
        self._pre = "sw_"
        self._name = name
        self._hub = hub
        self._state = False
        self._icon = icon
        self._data = None
        self._available = 1

    @property
    def is_on(self):
        """Return is_on status."""
        return self._state

    async def async_turn_on(self):
        """Turn On method."""
        _LOGGER.error(
            "Sending ON request to SWITCH device %s (%s)", self._name
        )
        if not self._hub._client.connected:
            self._hub._client.connect()
        self._hub._client.write_coil(address=400,value=True)
        self._state = STATE_ON
        self.schedule_update_ha_state()

    async def async_turn_off(self):
        """Turn Off method."""
        _LOGGER.error(
            "Sending OFF request to SWITCH device %s (%s)",  self._name
        )
        if not self._hub._client.connected:
            self._hub._client.connect()
        self._hub._client.write_coil(address=400,value=False)
        self._state = STATE_OFF
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
    def _update_state(self):
        _LOGGER.debug("REFRESHING SWITCH via update_state %s - %s", self._name)
        self._available = 0
        if self._hub._client.connected:
            self._available = 1
            chargestate_data = self._hub._client.read_coils(address=400, count=1, slave=0)
            charging = chargestate_data.bits[0]
            if charging:
                self._state = STATE_ON
            else:
                self._state = STATE_OFF
            _LOGGER.debug(self._state)
            return self._state
        else:
            _LOGGER.debug("Hub not connected - SWITCH %s - %s", self._name, self)
            self._available = 0
        return False

    async def async_update(self):
        """Return sensor state."""
        self._data = self.hass.data[DOMAIN]["data"]
        _LOGGER.debug("REFRESHING SWITCH %s - %s", self._name)
        self._available = 0
        if self._hub._client.connected:
            self._available = 1
            chargestate_data = self._hub._client.read_coils(address=400, count=1, slave=0)
            charging = chargestate_data.bits[0]
            if charging:
                self._state = STATE_ON
            else:
                self._state = STATE_OFF
            _LOGGER.debug(self._state)
            return self._state
        else:
            _LOGGER.debug("Hub not connected - SWITCH %s - %s", self._name, self)
            self._available = 0
        return False
