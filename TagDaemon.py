#Copyright (C) 2021,2022 Andrew Palardy
#See LICENSE file for complete license terms
#Main file of StorageTags
from TDMqttClient import TDMqttClient
from TDCameraDecoder import TDCameraDecoder
import time
import yaml

def Main():
    #Objects cache
    Objs = {}
    #Open the configuration yaml file
    CFname = "config.yml"
    print("MAIN: Opening configuration file ",CFname)
    CFile = open(CFname,'r')
    Config = yaml.safe_load(CFile)
    print("CONFIG: Entire configuration structure is ",Config)


    #If MQTT section is not none, start MQTT
    ConfigMQTT = Config.get('mqtt')
    Objs['MqttCl'] = None
    if ConfigMQTT is not None:
        print("CONFIG: Creating MQTT")
        Objs['MqttCl'] = TDMqttClient(ConfigMQTT)
    else:
        print("CONFIG: MQTT not defined, unable to function")
        exit()

    #For each entry in the Cameras array, start the camera
    ConfigCams = Config.get('cameras')
    Objs['CamCd'] = []
    if ConfigCams is not None:
        print("CONFIG: Creating",len(ConfigCams),"Cameras")
        for Cam in ConfigCams:
            Objs['CamCd'].append(TDCameraDecoder(Cam,Objs['MqttCl']))
    else:
        print("CONFIG: No cameras defined, not starting module")

    #MainLoop
    while(1):
        try:
            time.sleep(10)
        except:
            break

    #Send stop command to other threads
    if Objs['MqttCl'] is not None:
        Objs['MqttCl'].stop()
    for Cam in Objs['CamCd']:
        if Cam is not None:
            Cam.stop()

#Entry point
if __name__ == "__main__": 
    Main() 
