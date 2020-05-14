class name:
    def fname(self,namee):
        self.namee=namee
        print("the name of the student is ",self.namee)

class rollno:
    def roll(self,rno):
        self.rno=rno
        print("the name of the student is ",self.rno)

class phone(name,rollno):
    def number(self,phno):
        self.phno=phno
        print("the name of the student is ",self.phno)

s=phone()
Name=input("Enter the name :")
Rollno=input("Enter roll number: ")
Phone=input("Enter phone number :")
s.fname(Name)
s.roll(Rollno)
s.number(Phone)