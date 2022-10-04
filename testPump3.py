import RPi.GPIO as GPIO
from datetime import datetime
import time

RelayPin = 4
Sensor = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(RelayPin,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(Sensor,GPIO.IN)
    




def command():
    for i in range(0, 30):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        time.sleep(1)
        if GPIO.input(Sensor) == 1:
            detect = "\nWater Detected  " + str(current_time)
  

            # Command one actuator using RaspBerry Pi Zero W GPIO (4)
            
            GPIO.output(RelayPin,GPIO.LOW)
            print(detect)
        elif GPIO.input(Sensor) == 0:
            not_detected = "\nWater Not Detected " + str(current_time)
            print(not_detected)
            GPIO.output(RelayPin,GPIO.HIGH)

command()