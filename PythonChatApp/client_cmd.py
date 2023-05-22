# DEVEELOPED BY HOSEIN MOHAMADPOR
import threading
import socket
import time

c = ('localhost' , 50001)

client = socket.socket()
client.connect(c)
print("GOT new connection")

def recv():
    while(True):
        data_get = client.recv(1024).decode("utf-8")
        print(data_get)
        time.sleep(5)

def send():
    while(True):
        text = input(">>CLIENT>>").encode("utf-8")
        client.send(text)
        time.sleep(5)
    
threading.Thread(target=send).start()
threading.Thread(target=recv).start()