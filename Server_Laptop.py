import mysql.connector
import socket
from datetime import datetime

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1060
SIZE = 1024
FORMAT = "utf-8"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
print('Starting The Server at: ', datetime.now())
print("Waiting to accept a new connection")
sock.listen(5)
client, addr = sock.accept()
print("""q : for close connection
on : for turn the light on
off: for turn the light off
        """)

# Send actuator data over TCP/IP socket communication to RaspBerry Pi Zero W (8)

while True:
    message_to_client = input("Command the actuator: ")
    message_to_client_encode = message_to_client.encode(
        'utf-8')
    client.send(message_to_client_encode)
    if message_to_client == 'q':
        break

# Receive sensor data and datetime over TCP/IP socket communication from RaspBerry Pi Zero W using Python (5)

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

# Store sensor data and datetime in a persistent media (MySQL or local file) (6)

dataBase = mysql.connector.connect(

    host="localhost",

    user="root",

    passwd="",

    database="hdsd"
)


cursorObject = dataBase.cursor()
f = open("Report.txt", "r")
end_of_file = f.readline()
for x in f:
    res = x.split()
    sql = "INSERT INTO STUDENT (NAME, EMAIL) VALUES (%s, %s)"
    val = (str(res[0]), str(res[1]))
    cursorObject.execute(sql, val)
    dataBase.commit()
    if not end_of_file:
        break