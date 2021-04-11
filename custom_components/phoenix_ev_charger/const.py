DOMAIN = "phoenix_ev_charger"
DEFAULT_NAME = "Walli"
DEFAULT_SCAN_INTERVAL = 60
DEFAULT_PORT = 502
DEFAULT_DEVICE_MODEL = "EV-CC-AC1-M3"
CONF_PEVC_HUB = "pevc_hub"
CONF_DEVICE_MODEL = "device_model"
ATTR_MANUFACTURER = "Phoenix Contact"

PHOENIX_DEVICE_VARIANTS = {
    "EV-CC-AC1-M3",
    "EM-CP-PP",
}

SENSOR_TYPES = {
    "SN": ["Serial Number", "sn", None, None],
    "DeviceName": ["Device name", "devicename", None, None],
    "Current": ["Current (PWM)", "current", "A", "mdi:current-ac"],
    "DeviceState": ["Device state", "devstate", None, None],
    "FirmwareVersion" : [ "Firmware version", "fwvers", None, None],
}

DEVICE_STATUSSES = {
    'A' : "State A",
    'B' : "State B",
    'C' : "State C",
    'D' : "Errorstate D",
    'E' : "Errorstate E",
}

