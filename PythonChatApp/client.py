import socket

c = ('localhost' , 50001)

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

client.connect(c)
print("GOT new connection")

while(True):
    data = client.recv(1024).decode("utf-8")
    print(data)