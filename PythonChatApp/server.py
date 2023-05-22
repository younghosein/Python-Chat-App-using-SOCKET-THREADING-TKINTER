# DEVEELOPED BY HOSEIN MOHAMADPOR
import socket
import string

s = ('localhost' , 50001)

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind(s)

server.listen(2)

con , addr = server.accept()
print("RECEIVED connection from", addr)

while(True):
    sd=input(">>>  ").encode("utf-8")
    con.send(sd)