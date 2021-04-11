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
    "DeviceState": ["Device State (A-F)", "devstate", None, None],
    "EnergyChargeSequence": ["Energy Charge Sequence", "chargesequence", "Wh", "mdi:energy"],
    "ActualChargeCurrentSetting": ["Actual Charge Current Setting", "chargecurrentsetting", "A",
                                   "remoteChargeCurrentLimitation"],
    "RemoteChargeCurrentLimitation": ["Remote Charge Current Limitation", "remotechargecurrentlimit", "A",
                                      "remoteChargeCurrentLimitation"],
    "CableAssemblyCapability": ["Capability of Cable Assembly", "cablecapability", "A",
                                "remoteChargeCurrentLimitation"],
    "ActiveChargingDuration": ["Active Charging Duration", "chargingduration", "s", "mdi:time"],
    "DigInLD": ["Digital In LD", "diginld", None, None],
    "DigInEN": ["Digital In EN", "diginen", None, None],
    "DigInML": ["Digital In ML", "diginml", None, None],
    "DigInXR": ["Digital In XR", "diginxr", None, None],
    "DigInIN": ["Digital In IN", "diginin", None, None],
    "DigOutER": ["Digital Out ER", "digouter", None, None],
    "DigOutLR": ["Digital Out LR", "digoutlr", None, None],
    "DigOutVR": ["Digital Out VR", "digoutvr", None, None],
    "DigOutCR": ["Digital Out CR", "digoutcr", None, None],
    "DeviceName": ["Device name", "devicename", None, None],
    "MacAddress": ["MAC address", "macaddress", None, None],
    "SerialNumber": ["Serial Number", "serialnr", None, None],
    "FirmwareVersion": ["Firmware version", "fwvers", None, None],
}

DEVICE_STATUSSES = {
    '0': "offline",
    'A': "State A",
    'B': "State B",
    'C': "State C",
    'D': "Errorstate D",
    'E': "Errorstate E",
}
