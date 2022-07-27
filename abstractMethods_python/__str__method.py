class Student:
    def __init__(self,name,rollno):
        self.name=name 
        self.rollno=rollno 
        
    def __str__(self):
        return "this is student with name:{} and roll:{}".format(self.name,self.rollno)
    
s1=Student("john",27)
s2=Student("seam",54) 
print(s1)
print(s2)   