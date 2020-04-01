#! /usr/bin/python3
 
import paho.mqtt.client as mqtt
import time

verbose = False

def on_log(client, userdata, level, buf):
    print("log: "+buf)
    
def on_connect(client, userdata, flags, rc):
    if rc==0:
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

#  on_message will get messages from the topics subscribed to
def on_message(client,userdata,msg):
    topic=msg.topic
    msgPayload=str(msg.payload)
    print("Topic: ",topic)
    print("Message: ",msgPayload)
        
def on_disconnect(client, userdata, flags, rc=0):
    print("Disconneted result code "+str(rc))
        
broker="192.168.0.3"
client = mqtt.Client("Broker_1")

client.on_connect=on_connect
if verbose:
    client.on_log=on_log
client.on_message=on_message
client.on_disconnect=on_disconnect

print("Connecting to broker ",broker)
client.connect(broker)
client.loop_start()
client.subscribe("topic_test")
time.sleep(10)
client.publish("topic_test","Python 3 message from Broker_1")

time.sleep(30)

client.publish("topic_test", "Broker_1  about to disconnect")
time.sleep(30)

client.loop_stop()
client.disconnect()
