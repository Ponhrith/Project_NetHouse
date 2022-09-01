import RPi.GPIO as GPIO
import time
from datetime import datetime


channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(channel, GPIO.IN)
GPIO.setup(18,GPIO.OUT)

f = open("Report.txt", "r")
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
#while True:
time.sleep(1)
#    break 

import socket

HOST = "172.16.0.191"
PORT = 1060
ADDR = (HOST, PORT)
max_size = 1024
FORMAT = "utf-8"
print("Starting the client at: ", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def main():
    # Staring a TCP socket. #
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to the server. #
    client.connect(ADDR)

    # Opening and reading the file data. #
    file = open("Report.txt", "r")
    data = file.read()

    # Sending the filename to the server. #
    client.send("from client.txt".encode(FORMAT))
    msg = client.recv(max_size).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    # Sending the file data to the server. #
    client.send(data.encode(FORMAT))
    msg = client.recv(max_size).decode(FORMAT)
    print(f"[SERVER]: {msg}")

    # Closing the file. #
    file.close()

    # Closing the connection from the server. #
    client.close()


if __name__ == "__main__":
    main()

# Receiving command from your Laptop or Desktop over TCP/IP socket communication using Python and command your actuator (3)


import socket

HOST = "172.16.0.191"
PORT = 1060
ADDR = (HOST, PORT)
max_size = 1024
FORMAT = "utf-8"
print("Starting the client at: ", datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)