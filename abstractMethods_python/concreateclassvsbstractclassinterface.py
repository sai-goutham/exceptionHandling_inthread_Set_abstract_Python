#concrete class and abstract class vs interface :
from abc import * 
class Auto(ABC):
    @abstractmethod 
    def m1(self):pass 
    @abstractmethod 
    def m2(self):pass
    @abstractmethod 
    def m3(self):pass 
class AbsCls(Auto):
    def m1(self):
        print("m1 method implementation")
    def m2(self):
        print("m2 method implementation")

class  Concrete(AbsCls):
    def m3(self):
        print("m3 method implementation")

c=Concrete
c.m1()
c.m2()
c.m3()                    

#oops4 material