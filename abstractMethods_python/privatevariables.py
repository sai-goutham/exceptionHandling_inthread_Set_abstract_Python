#how to access private variables from outside of class 

class test:
    def __init__(self):
        self.__x=10
        
t=test()
print(t._test__x)