#Copyright (C) 2021,2022 Andrew Palardy
#See LICENSE file for complete license terms
#Viewer application for TagDaemon
from paho.mqtt import client as mqtt_client
import json
import cv2
import numpy as np
import sys
import getopt


#Help description
def printHelp():
    print('Usage:')
    print('TDViewer.py -b <broker address> -u <broker username> -p <broker password> -r <broker port>')
    exit(2)


#Process arguments
broker = None
user = None
passwd = None
port = 1883
try:
    opts, args = getopt.getopt(sys.argv[1:],"b:u:p:r:",["broker=","user=","pass=","port="])
except getopt.GetoptError:
    printHelp()
for opt,arg in opts:
    if opt in ("-b","--broker"):
        broker = arg
    elif opt in ("-u","--user"):
        user = arg
    elif opt in ("-p","--pass"):
        passwd = arg
    elif opt in ("-r","--port"):
        port = int(arg)

if broker is None:
    print("Broker address not provided!")
    printHelp()

#Establish connection to broker
client = mqtt_client.Client("TDViewer")

#If Username is none, skip auth
if(user is not None):
    if(passwd is None):
        print("MQTT: Error: Username is valid, but Password is None")
        print("MQTT: Not using authentication")
    else:
        client.username_ps_set(user,passwd)


#Start the broker
client.connect(broker,port)