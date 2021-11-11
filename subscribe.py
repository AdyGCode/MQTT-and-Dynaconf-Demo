# ---------------------------------------------------------------------
# Filename      : subscribe.py
# Location      : ./
# Project       : MQTT-Demo
# Author        : Adrian Gould <adrian.gould@nmtafe.wa.edu.au>
# Created       : 11/11/21
# Version       : 0.1
# Description   :
#   This is a description of what the file is for
#
# ---------------------------------------------------------------------


import paho.mqtt.client as mqtt_client
from config import settings
import random
import time

client_id = f'{settings.client_prefix}-{random.randint(0, 1000)}'


def connect_mqtt() -> mqtt_client:
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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(settings.topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
