import json
import sqlite3
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

def sql_create_table():
    #create table for credentials
    try:
        conn = sqlite3.connect("aqmCredMan/credentials.sqlite")
        cursor = conn.cursor()
        conn.execute(open("aqmCredMan/sql/create_table.sql", "r").read())
        conn.close()
    except Exception as e:
        logging.info(e)
        return False

def get_new_id():
    conn = sqlite3.connect("aqmCredMan/credentials.sqlite")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM credentials ORDER BY id DESC LIMIT 0, 1")
    output = cursor.fetchall()
    conn.close()
    if output == []:
        return 1
    return int(output[0][0]) + 1

def sql_insert_credentials(id,username,password):
    conn = sqlite3.connect("aqmCredMan/credentials.sqlite")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO credentials VALUES (?,?,?)",(id,username,password))
    conn.commit()
    conn.close()
def create_response():
    sql_create_table()
    id = get_new_id()
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
        "id":id,
        "web_username": web[0],
        "web_password": web[1]
    }
    sql_insert_credentials(id,web[0],web[1])
    logging.info(response)
    return json.dumps(response)