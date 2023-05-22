# DEVEELOPED BY HOSEIN MOHAMADPOR
import threading
import socket
import time

s = ('localhost' , 50001)

server = socket.socket()
server.bind(s)
server.listen(2)
con , addr = server.accept()
print("RECEIVED connection from", addr)

def send_data():
    while(True):
        send=input(">>SERVER>> ").encode("utf-8")
        con.send(send)
        time.sleep(5)
        #Convert
        #str(send)

def recv_data():
    while(True):
        data_recv = con.recv(1024).decode("utf-8")
        print(data_recv)
        time.sleep(5)
    
threading.Thread(target=send_data).start()
threading.Thread(target=recv_data).start()