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

DIGITAL_OUT_FUNCTIONS = {
    0:  "Inaktiv1Ladesteuerung im Status A",
    2:  "Ladesteuerung im Status B",
    3:  "Ladesteuerung im Status B und PWM EIN",
    4:  "Ladesteuerung im Status B und PWM AUS",
    5:  "Ladesteuerung im Status C",
    6:  "Ladesteuerung im Status D",
    7: "Ladesteuerung im Status E",
    8: "Ladesteuerung im Status F",
    9: "Ladesteuerung im Status A oder B",
    10: "Ladesteuerung im Status A oder B und PWM EIN",
    11: "Ladesteuerung im Status A oder B und PWM AUS",
    12: "Ladesteuerung im Status A, B oder C",
    13: "Ladesteuerung im Status A, B oder D",
    14: "Ladesteuerung im Status A bis D",
    15: "Ladesteuerung im Status E oder F (Default für Ausgang ER)",
    16: "Ladesteuerung im Status C oder D (Default für Ausgang VR)",
    17: "PWM EIN (Default für Ausgang CR)",
    18: "Gültiger Proximity erkannt",
    19: "Ungültiger Proximity erkannt",
    20: "13-A-Ladestecker erkannt",
    21: "20-A-Ladestecker erkannt",
    22: "32-A-Ladestecker erkannt",
    23: "63-A-Ladestecker erkannt",
    24: "13-A- oder 20-A-Ladestecker erkannt",
    25: "13-A-, 20-A- oder 32-A-Ladestecker erkannt",
    26: "Ladestecker mit geringer Stromtragfähigkeit abgewiesen",
    27: "Ladesteuerung schaltet das Ladeschütz EIN",
    28: "Status D Belüftung an",
    29: "Verriegelung aktiv (Default für Ausgang LR)",
    30: "Register Ausgang 1",
    31: "Register Ausgang 2",
    32: "Register Ausgang 3",
    33: "Register Ausgang 4",
    34: "Überstrom detektiert",
    35: "Ladeschützüberwachung ausgelöst",
    36: "Status D, Fahrzeug abgewiesen",
    37: "Fahrzeug angeschlossen im Status B oder C oder D",
    38: "Reserviert für zukünftige Funktion",
    39: "Autorisierungsstatus (Blinken: Autorisierung in Arbeit, Permanent: Freigabe liegt vor)",
}

DIGITAL_IN_FUNCTIONS = {
    0: "Inaktiv1Freigabe Ladevorgang permanentes High-Signal (Default für Eingang EN)",
    2: "Verfügbarkeit Ladestation (Default für Eingang XR)",
    3: "Rückmeldung Verriegelung Ladestecker (Default für Eingang LD)",
    4: "Verriegelung (permanentes High-Signal)",
    5: "Schützüberwachung über NO-Hilfskontakt",
    6: "Schützüberwachung über NC-Hilfskontakt",
    7: "PWM-Signal auf 5 %",
    8: "Ladestrom auf 6 A",
    9: "Ladestrom auf 10 A",
    10: "Ladestrom auf 13 A",
    11: "Ladestrom auf 16 A (Default für Eingang IN)",
    12: "Ladestrom auf 20 A",
    13: "Ladestrom auf 32 A",
    14: "Ladestrom auf 63 A",
    15: "Ladestrom auf 70 A",
    16: "Freigabe Ladevorgang gepulstes Signal",
    17: "Verriegelung (gepulstes Signal) (Default für Eingang ML)",
    18: "Reserviert für zukünftige Funktion",
    19: "Ladestrom auf zulässigen Maximalwert",
    20: "Ladevorgang pausieren (OCPP: Suspend EVSE)",
    21: "Fehlerzustand erzeugen",
}
