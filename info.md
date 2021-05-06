
# home-assistant-phoenix-ev-charger

Home Assistant Integration for communicating with Phoenix Contact EV Charge Controllers found e.g. in ESL "Walli LIGHT" and "Walli LIGHT pro" wallboxes. Communication s done via Modbus TCP, so no username/password is needed. 

Currently only Phoenix Contact EV-CC-AC1-M3-xx charge controllers (Walli Light pro) are tested (works for me).

EM-CP-PP-ETH charge controllers (Walli Light) should work mostly, but some values will be not correct (different registers). This will be fixed (hopefully soon).

![Walli Wallbox](/images/walli_light.webp)


![EV-CC-AC1-M3](/images/pro.jpg) 
![EM-CP-PP-ETH](/images/light.jpg)


Heavily based on [`home-assistant-saj-modbus`](https://github.com/wimb0/home-assistant-saj-modbus) from [@wimb0](https://github.com/wimb0).

## Installation
To install via HACS, please add https://github.com/abrlox/home-assistant-phoenix-ev-charger as custom repository to HACS.
Now you can add the integration to HACS.

After Rebooting your system, you can search for "Phoenix EV Charger" on the HomeAssistant integration page and install it.

After reboot of Home-Assistant, this integration can be configured through the integration setup UI

