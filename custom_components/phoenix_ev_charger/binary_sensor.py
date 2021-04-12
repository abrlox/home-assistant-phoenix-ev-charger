import logging
from typing import Any, Dict, Optional

from homeassistant.const import CONF_NAME
from homeassistant.core import callback
from homeassistant.helpers.entity import Entity

from .const import ATTR_MANUFACTURER, DEVICE_STATUSSES, DOMAIN, BINARY_SENSOR_TYPES, DIGITAL_STATUS

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, entry, async_add_entities):
    hub_name = entry.data[CONF_NAME]
    hub = hass.data[DOMAIN][hub_name]["hub"]

    device_info = {
        "identifiers": {(DOMAIN, hub_name)},
        "name": hub_name,
        "manufacturer": ATTR_MANUFACTURER,
    }

    entities = []
    for binary_sensor_info in BINARY_SENSOR_TYPES.values():
        binary_sensor = PevcBinary_sensor(
            hub_name,
            hub,
            device_info,
            binary_sensor_info[0],
            binary_sensor_info[1],
            binary_sensor_info[2],
            binary_sensor_info[3],
        )
        entities.append(binary_sensor)

    async_add_entities(entities)
    return True


class PevcBinary_sensor(Entity):
    """Representation of an PEVC Modbus binary_sensor."""

    def __init__(self, platform_name, hub, device_info, name, key, unit, icon):
        """Initialize the binary_sensor."""
        self._platform_name = platform_name
        self._hub = hub
        self._key = key
        self._name = name
        self._unit_of_measurement = unit
        self._icon = icon
        self._device_info = device_info
        self._is_on = False


    async def async_added_to_hass(self):
        """Register callbacks."""
        self._hub.async_add_pevc_binary_sensor(self._modbus_data_updated)

    async def async_will_remove_from_hass(self) -> None:
        self._hub.async_remove_pevc_binary_sensor(self._modbus_data_updated)

    @callback
    def _modbus_data_updated(self):
        self.async_write_ha_state()

    @callback
    def _update_state(self):
        if self._key in self._hub.data:
            self._state = self._hub.data[self._key]

    @property
    def name(self):
        """Return the name."""
        return f"{self._platform_name} {self._name}"

    @property
    def unique_id(self) -> Optional[str]:
        return f"{self._platform_name}_{self._key}"

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    @property
    def icon(self):
        """Return the binary_sensor icon."""
        if self._key in self._hub.data:
            if self._hub.data[self._key] == DIGITAL_STATUS[True]:
                return "mdi:lightbulb-on"
            else:
                return "mdi:lightbulb-outline"
        return self._icon

    @property
    def state(self):
        """Return the state of the binary_sensor."""
        if self._key in self._hub.data:
            return self._hub.data[self._key]

    @property
    def state_attributes(self) -> Optional[Dict[str, Any]]:
        return None

    @property
    def should_poll(self) -> bool:
        """Data is delivered by the hub"""
        return False

    @property
    def is_on(self) -> bool:
        if self._key in self._hub.data:
            return self._hub.data[self._key] == DIGITAL_STATUS[True]

    @property
    def device_info(self) -> Optional[Dict[str, Any]]:
        return self._device_info
