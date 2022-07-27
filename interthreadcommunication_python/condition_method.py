from threading import * 
def consume(c):
    c.acquire()
    print("consumer waiting for update")
    c.wait()
    print("consumer got notification &consuming the item")
    c.release()
    
def produce(c):
    c.acquire()
    print("producer producing items")
    print("produce giving notification")
    c.notify()
    c.release()
    
c=Condition()
t1=Thread(target=consume,args=(c,))
t2=Thread(target=produce,args=(c,))
t1.start()
t2.start()