import RPi.GPIO as GPIO
import time
from datetime import datetime
from gpiozero import LED
import socket



#channel = 21
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.setup(4, GPIO.IN)
#GPIO.setup(channel, GPIO.IN)
#GPIO.setup(18,GPIO.OUT)

#f = open("Report.txt", "r")
# def callback(channel):
#     if GPIO.input(channel):
#         print("no water detected")
       
#         GPIO.output(18,GPIO.LOW)
        
#     else:
#         print("water detected")
#         GPIO.output(18,GPIO.HIGH)
        

# GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) # let us know when pin goes HIGH or LOW
# GPIO.add_event_callback(channel, callback) #assign function to GPIO PIN, Run function on change

# #infinite loop
# #while True:
# time.sleep(1)
# #    break 



HOST = "172.16.0.191"
PORT = 1060
ADDR = (HOST, PORT)
max_size = 1024
FORMAT = "utf-8"
led = LED(18)
led_server = LED(17)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)
f = open("/home/pi/Documents/Report.txt", "a")
print("Starting the client at: ", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print("""q : for close connection
on : for turn a light on
off: for turn a light off
        """)




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





# Receiving command from your Laptop or Desktop over TCP/IP socket communication using Python and command your actuator (3)



def received():
    while True:
        data = client.recv(max_size)
        if data.decode('utf-8') == 'on':
            led_server.on()
            print("light is on")
        elif data.decode('utf-8') == 'off':
            led_server.off()
            print("light is off")
            print("At ", datetime.now(),
                  "server replied with: ", data.decode('utf-8'))
        if data.decode('utf-8') == 'q':
            break
command()
received()

f = open("/home/pi/Documents/Report.txt", "r")
data = f.read()
client.send("Report.txt".encode(FORMAT))
msg = client.recv(max_size).decode(FORMAT)
print(f"server: {msg}")
client.send(data.encode(FORMAT))
msg = client.recv(max_size).decode(FORMAT)
print(f"server: {msg}")
f.close()
client.close()
