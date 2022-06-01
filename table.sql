CREATE TABLE IF NOT EXISTS credentials (
    id INT NOT NULL IDENTITY(1,1),
    enterprise_user TEXT,
    enterprise_pass TEXT,
    enterprise_ssid TEXT,
    private_ssid TEXT,
    private_password TEXT,
    sense_net_name TEXT,
    mqtt_server TEXT,
    mqtt_username TEXT,
    mqtt_password TEXT,
    web_username TEXT,
    web_password TEXT
);