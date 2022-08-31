import RPi.GPIO as GPIO
import time


channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(18,GPIO.OUT)

def callback(channel):
    if GPIO.input(channel):
        print("no water detected")
       
        GPIO.output(18,GPIO.LOW)
        
    else:
        print("water detected")
        GPIO.output(18,GPIO.HIGH)
        

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) # let us know when pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback) #assign function to GPIO PIN, Run function on change

#infinite loop
while True:
    time.sleep(1)