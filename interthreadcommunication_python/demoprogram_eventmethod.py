from threading import * 
import time 
def trafficpolice():
    while True:
        time.sleep(10)
        print("traffic police giving green signal")
        even.set()
        time.sleep(20)
        print("traffic police giving red signal")
        even.clear()
        
def driver():
    num=0 
    while True:
        print("rider waiting for green signal")  
        even.wait()
        print("traffic signal is Green>>>>Vehicles can move")
        while even.isSet():
            num=num+1 
            print("vehicles No:",num,"crossing the signal")
            time.sleep(2) 
        print("traffic signal is Red....rider have to wait")
even=Event()
t1=Thread(target=trafficpolice)
t2=Thread(target=driver)
t1.start()
t2.start()             