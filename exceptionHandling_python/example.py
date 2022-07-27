class tooyoung(Exception):
    def __init__(self,arg):
        self.msg=arg 
class tooold(Exception):
    def __init__(self,arg):
        self.msg=arg 
n=int(input("enter a number"))
if n>60:
    raise tooyoung("cant marry now")
elif n<10:
    raise tooold("wait some time")
else:
    print("thanks")    
    
    