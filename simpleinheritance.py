class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printable(self):
        print(self.fname,self.lname)

p=person('sandeep','das')
p.printable()