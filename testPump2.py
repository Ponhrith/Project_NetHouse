import RPi.GPIO as GPIO
import time
from datetime import datetime
from gpiozero import LED
import socket

channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(4,GPIO.OUT)

def callback(channel):
    if GPIO.input(channel):
        print("no water detected")
       
        GPIO.output(4,GPIO.LOW)
        
    else:
        print("water detected")
        GPIO.output(4,GPIO.HIGH)
        
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel, callback) 

time.sleep(30)