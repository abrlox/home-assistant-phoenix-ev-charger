
# home-assistant-phoenix-ev-charger

Home Assistant custom component for communicating with Phoenix Contact EV Charge Controllers via ModBus TCP.
These Charge controllers for electric vehicles are found in some wallboxes, manufactured e.g. by ESL mobility like "Walli Light" and "Walli Light Pro".

Features:

* Installation through Config Flow UI
* Configurable polling interval
* No password protected acces through WebApi needed
* Support for EV-CC-AC1-M3-xx controllers tested
* EM-CP-PP-ETH controllers should also work, but some values are missing so far

Configuration

* Add https://github.com/abrlox/home-assistant-phoenix-ev-charger as custom repository to HACS
* Add Phoenix EV Charger to HACS integrations
* Go to the integrations page in your configuration and click on new integration -> Phoenix EV Charger

Comments and Remarks are always welcome!