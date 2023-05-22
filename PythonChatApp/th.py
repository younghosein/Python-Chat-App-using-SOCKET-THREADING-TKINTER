# DEVEELOPED BY HOSEIN MOHAMADPOR
import threading
import time

def hello1():
    while(True):
        print("hello")
        time.sleep(3)
    
def goodbye1():
    while(True):
        print("goodbye")
        time.sleep(1)

def hello2():
    while(True):
        print("Nigga")
        time.sleep(3)
    
def goodbye2():
    while(True):
        print("HAAAA")
        time.sleep(1)

thread1 = threading.Thread(target = hello1)
thread2 = threading.Thread(target = goodbye1)
thread3 = threading.Thread(target = hello2)
thread4 = threading.Thread(target = goodbye2)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

print("thread")