#parent class abstract method should be implemented in child classes.otherwise we cannot instantiate child class.if we are not creating child class
#object then we wont get any error 

from abc import *
class Ve(ABC):
    @abstractmethod 
    def wheels(self):
        pass 
    
class BUs(Ve):pass
 
#it is valid ..we are not creating child class object 

#note:if we are extending abstract class and does not override its abstract method then child class is also abstract and instantiation is not possible 

from abc import *
class v(ABC):
    @abstractmethod 
    def wheels(self):
        pass 

class bus(v):
    def wheels(self):
        return 7 

class Auto(v):
    def wheels(self):
        return 3 
    
b=bus()
print(b.wheels())

a=Auto()
print(a.wheels())
