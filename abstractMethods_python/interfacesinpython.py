#in general if an abstract class contains only abstract methods such type of abstract class is interface 
from abc import *
class DBinterface(ABC):
    @abstractmethod 
    def connect(self):pass 
    
    @abstractmethod 
    def disconnect(self):pass 
    
class Oracle(DBinterface):
    def connect(self):
        print("connecting")
    def disconnect(self):
        print("disconnecting")

class sybase(DBinterface):
    def connect(self):
        print("connecting base....")
    def disconnect(self):
        print("disconnect to base>>")
        
dbname=input('enter database name...')
classname=globals()[dbname] #the inbuilt globals()[string] converts string into class name and returns class name
x=classname()
x.connect()
x.disconnect()    


#reading class name from file

from abc import *
class Printer(ABC):
    @abstractmethod 
    def printit(self,text):pass 
    
    @abstractmethod 
    def disconnect(self):pass 
    
class EPson(Printer):
    def printit(self,text):
        print('printing from printer>>>')
        print(text)
    def disconnect(self):
        print("printing completed printer  ") 
        
class HP(Printer):
    def printit(self,text):
        print("printing from ")
        print(text) 
    def disconnect(self):
        print("printing completed on ")
                      
      
with open('config.txt','r') as f:
    pname=f.readline()

classname=globals()[pname] 
x=classname()
x.printit("this data has to print...")
x.disconnect()   
      
    
                        
