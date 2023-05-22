# DEVEELOPED BY HOSEIN MOHAMADPOR
import threading
import socket
import time
from tkinter import *

ip=""

r1=Tk()

def ip_get():
    global ip
    ip = get_ip.get()
    r1.destroy()

get_ip =Entry(r1)
label1=Label(r1,text="Enter IP:")
b1=Button(r1,text="set ip",command=ip_get)

label1.grid()
get_ip.grid()
b1.grid()

r1.mainloop()

c=(ip, 50002)
client=socket.socket()
client.connect(c)
print("GOT new connection from ",ip)

root = Tk()

canvas =Canvas(root)
scrollbar = Scrollbar(root,orient="vertical",command=canvas.yview)
frame = Frame(canvas)

def send():
    data_send=get_text.get().encode("utf-8")
    if(data_send!=""):
        client.send(data_send)
        label=Label(root,text=data_send,bg="red",fg="white")
        label.pack(fill=X,side=TOP)
        get_text.delete(0,END)

def recv():
    while(True): 
        data_recv=client.recv(1024).decode("utf-8")
        label2=Label(root,text=data_recv,bg="blue",fg="white")
        label2.pack(fill=X,side=TOP)
        
def update():
    while(True):
        canvas.configure(scrollregion=canvas.bbox('all'),yscrollcommand=scrollbar.set)
        time.sleep(1)

button=Button(root,text="send",command=send)
get_text=Entry(root)
button.pack(fill=X,side=BOTTOM)
get_text.pack(fill=X,side=BOTTOM)

canvas.pack(fill="both",side="left",expand=True)
scrollbar.pack(fill="y",side="right")
canvas.create_window(0,0,anchor='nw',window=frame)
canvas.update_idletasks()

threading.Thread(target=recv).start()
threading.Thread(target=update).start()

root.geometry("400x600")
root.title("client")
root.resizable()

root.mainloop()