# ---------------------------------------------------------------------
# Filename      : publish.py
# Location      : ./
# Project       : MQTT-Demo
# Author        : Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created       : 11/11/21
# Version       : 0.1
# Description   :
#   This is a description of what the file is for
#
# ---------------------------------------------------------------------

from paho.mqtt import client as mqtt_client
from config import settings
import random
import time

client_id = f'{settings.client_prefix}-{random.randint(0, 1000)}'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(settings.username, settings.password)
    client.on_connect = on_connect
    client.connect(settings.broker, settings.port)
    return client


def publish(client):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(settings.topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()
