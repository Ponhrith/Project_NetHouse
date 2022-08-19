import Rpi.GPIO as GPIO #Pri.GPIO can be installed on Linux?
import time

#GPIO setup
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("no water detected")
        
    else:
        print("water detected")
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) # let us know when pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback) #assign function to GPIO PIN, Run function on change

#infinite loop
while True:
    time.sleep(1)