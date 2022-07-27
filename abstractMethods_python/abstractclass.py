#child class are responsible to provide implementation for parent class abstract method 


#some times implementations of a class is not complete ,such type of partially implementation class are called abstract class
from abc import *
class test:
    pass
t=test()

#in the above code we can create object for test class ,because it does not contain any abstract method


from abc import *
class test1(ABC):
    pass 
t=test1()  

#in the above code we can create object ,even it is derived from ABC class,because it does not contain any abstract method like @abstractmethod 




#case-3

from abc import *
class t:
    @abstractmethod 
    def m1(self):
        pass
c=t()

#we can create object even class contain abstract method because we are not extending ABC class


#case-5 
from abc import *
class v:
    @abstractmethod 
    def m1(self):
        print("hello")
t=v()
t.m1()


#conclusion :-if a class contain at least one abstract  method and if we are extending ABC class then instantiation is not possible 

#"abstract class with  abstract method instantiation is not possible"
       
    
    