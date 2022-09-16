import RPi.GPIO as GPIO
import time
from datetime import datetime
from gpiozero import LED
import socket

led = LED(18)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

def command():
    for i in range(0, 30):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        time.sleep(1)
        if GPIO.input(4) == 1:
            detect = "\nWater Detected  " + str(current_time)
            f.write(detect)

            # Command one actuator using RaspBerry Pi Zero W GPIO (4)
            
            led.on()
            print(detect)
        elif GPIO.input(4) == 0:
            not_detected = "\nWater Not Detected " + str(current_time)
            f.write(not_detected)
            print(not_detected)
            led.off()

command()