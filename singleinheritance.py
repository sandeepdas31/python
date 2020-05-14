class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printable(self):
        print("the name of the student is :",end="")
        print(self.fname,self.lname)
    
class student(person):
        def rollno(self,rno):
            self.rno=rno
            print("the roll no is: ",self.rno)
       

p=student('sandeep','das')
p.printable()
p.rollno(201603043)