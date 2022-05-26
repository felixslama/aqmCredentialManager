import json
import pyodbc
import random
import string
import logging
from urllib import response
from .config import *

#build json from credentials
def generate_user_pass_combo():
    aqm_user = "aqm"
    aqm_pass = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))
    return aqm_user, aqm_pass

web = generate_user_pass_combo()

def send_to_sql_server():
    try:
        #create credentials table
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + db_host + ';DATABASE=' + db_user + ';UID=' + db_user + ';PWD=' + db_pass)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO credentials (enterprise_user, enterprise_pass, enterprise_ssid, private_ssid, private_password, sense_net_name, mqtt_server, mqtt_username, mqtt_password, web_username, web_password) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
                       enterprise_user, enterprise_pass, enterprise_ssid, private_ssid, private_password, sense_net_name, mqtt_server, mqtt_username, mqtt_password, web[0], web[1])
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except Exception as e:
        logging.info(e)
        return False

def create_response():
    web = generate_user_pass_combo()
    response = {
        "enterprise_user": enterprise_user,
        "enterprise_pass": enterprise_pass,
        "enterprise_ssid": enterprise_ssid,
        "private_ssid": private_ssid,
        "private_password": private_password,
        "sense_net_name": sense_net_name,
        "mqtt_server": mqtt_server,
        "mqtt_username": mqtt_username,
        "mqtt_password": mqtt_password,
        "web_username": web[0],
        "web_password": web[1]
    }
    send_to_sql_server()
    logging.info(response)
    return json.dumps(response)