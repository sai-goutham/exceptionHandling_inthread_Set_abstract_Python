from threading import *
import time 
def producer():
    time.sleep(5)
    print("producer thread producing items:")
    print("producer thread giving notification by setting event")
    event.set()
def consumer(): 
    print("consumer thread is waiting for update")
    event.wait()
    print("consumer thread got notification and consuming items")
    
event=Event()
t1=Thread(target=producer)
t2=Thread(target=consumer) 
t1.start()
t2.start()      


