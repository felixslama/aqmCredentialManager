import json
import logging
from .config import *

#build json from credentials
credentials = {
    "enterprise_user": enterprise_user,
    "enterprise_pass": enterprise_pass,
    "enterprise_ssid": enterprise_ssid,
    "private_ssid": private_ssid,
    "private_password": private_password,
    "sense_net_name": sense_net_name,
    "mqtt_server": mqtt_server,
    "mqtt_username": mqtt_username,
    "mqtt_password": mqtt_password,
    "web_username": web_username,
    "web_password": web_password
}
def get_credentials():
    logging.info(credentials)
    logging.info(json.dumps(credentials))
    return json.dumps(credentials)