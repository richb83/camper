#! /usr/bin/python3

import paho.mqtt.client as mqtt
import time
import json
import os
import re

verbose = False
broker = "192.168.0.3"
broker_port = 1883
basePath = '/sys/bus/w1/devices'
fname = 'w1_slave'

# Topics
topic_con = "sensor_connection"
topic_temp = "sensor_temp"
topic_fan = "sensor_fan"


def get_temps():
    dictTemps = {}
    dirList = None
    if os.path.exists(basePath):
        dirList = os.listdir(basePath)
    if dirList:
        for d in dirList:
            if d != 'w1_bus_master1':
                tempData = ''
                fPath = os.path.join(basePath, d, fname)

                with open(fPath, 'r') as fo:
                    for line in fo:
                        matchObj = re.search(r't=(\d{4,})', line, re.I)
                        if matchObj:
                            tempData = matchObj.group(1)
                            #print('The temp is', tempData)
                celsius = float(tempData) / 1000
                farenheit = (celsius * 1.8) + 32
                dictTemps[d] = farenheit
    return dictTemps


def on_log(client, userdata, level, buf):
    print("log: "+buf)


def on_connect(client, userdata, flags, rc):
    # TODO  Send a message to show connection
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, rc):
    pass
    # TODO  Create a will statment to notify the dispaly that the connection was lost

# message(msg) has "topic" "payload" "qos" "retain"


def on_message(client, userdata, msg):
    pass
    # topic=msg.topic
    # msgPayload=str(msg.payload)
    # print("Topic: ",topic)
    # print("Message: ",msgPayload)


client = mqtt.Client(client_id="Sensor_1_Send", clean_session=True,
                     userdata="Sensor_1_Send")

if verbose:
    client.on_log = on_log
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker)

client.loop_start()
time.sleep(30)
data = get_temps()
client.publish(topic_temp, json.dumps(data))
