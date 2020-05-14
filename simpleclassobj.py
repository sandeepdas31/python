class person:
    
    def __init__(self,x,y):
        print("simple class object program")
        self.x=x
        self.y=y
        self.x+=self.y
    def fun(self,z):
        self.z=z
        print(z)
            
    
p1=person(30,20)
print(p1.x)
print(p1.y)
p1.fun(8745)
p1.fun("hello")