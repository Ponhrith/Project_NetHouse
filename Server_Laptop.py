# Receive sensor data and datetime over TCP/IP socket communication from RaspBerry Pi Zero W using Python (5)

import socket
from datetime import datetime
HOST = socket.gethostbyname(socket.gethostname())
PORT = 1060
SIZE = 1024
FORMAT = "utf-8"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
print('Starting The Server at: ', datetime.now())
print("Waiting For The Incoming Connection from client")
sock.listen(5)
client, addr = sock.accept()

while True:

    filename = client.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the filename.")

    file = open(filename, "w")
    client.send("Filename received.".encode(FORMAT))

    data = client.recv(SIZE).decode(FORMAT)
    print(f"[RECV] Receiving the file data.")
    file.write(data)
    client.send("File data received".encode(FORMAT))

    file.close()

    client.close()
    print(f"[DISCONNECTED] {addr} disconnected.")
    break

sock.close()



# Send actuator data over TCP/IP socket communication to RaspBerry Pi Zero W (8)

while True:
    message_to_client = input("Enter message to client: ")
    message_to_client_encode = message_to_client.encode(
        'utf-8')
    client.send(message_to_client_encode)
    if message_to_client == 'q':
        break
# Store sensor data and datetime in a persistent media (MySQL or local file) (6)

import mysql.connector
dataBase = mysql.connector.connect(

    host="localhost",

    user="root",

    passwd="",

    database="hdsd"
)


cursorObject = dataBase.cursor()
f = open("Light sensor.txt", "r")
end_of_file = f.readline()
for x in f:
    res = x.split()
    sql = "INSERT INTO tbl_STUDENT (NAME, EMAIL) VALUES (%s, %s)"
    val = (str(res[0]), str(res[1]))
    cursorObject.execute(sql, val)
    dataBase.commit()
    if not end_of_file:
        break