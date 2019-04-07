#!/usr/bin/python3

import os
import requests
import subprocess, platform
import time
import pychromecast
import socket

sensor_ip = '192.168.0.47'
chromecast_name = 'Google home'
mp3_server_port = "8888"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
mp3_server_ip = s.getsockname()[0]
s.close()

mp3_url = "http://"+mp3_server_ip+":"+mp3_server_port+"/alarme.mp3"

print ("Preparing chromecast...")
chromecasts = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if cc.device.friendly_name == chromecast_name)
cast.wait()
print("Chromecast is ready")

def pingSensor():
    global sensor_ip
    try:
        output = subprocess.check_output("ping -c 1 -i 0.1 "+sensor_ip, shell=True)
        return 1
    except:
        return 0

    return True

def triggerAlarm():
    global cast
    mc = cast.media_controller
    mc.play_media(mp3_url, 'audio/mp3')
    time.sleep(15)

def app():
    response = pingSensor()

    if response == 1:
        print("Sensor is up!")
        triggerAlarm()
        return True
    else:
        print("Sensor is down")
        return False

while True:
    app()
