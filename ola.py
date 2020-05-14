class micro:

    def micro1(self,km):
        self.km=km
        print("Thanks for selecting micro cabs")
        print("The max speed that a Micro cab go is 150 km per hour")
        print("The fair for per kilometer is rupees 12")
        self.km=12*self.km
        print("The total fair is: ",self.km)
class mini:

    def mini1(self,km):
        self.km=km
        print("Thanks for selecting mini cabs")
        print("The max speed that a Mini cab go is 180 km per hour")
        print("The fair for per kilometer is rupees 15")
        self.km=15*self.km
        print("the total fair is: ",self.km)

class prime:

    def prime1(self,km):
        self.km=km
        print("thanks for selecting prime cabs")
        print("The max speed that a Prime cab go is 210 km per hour")
        print("The fair for per kilometer is rupees 18")
        self.km=18*self.km
        print("The total fair is: ",self.km)

class sedan:

    def sedan1(self, km):
        self.km = km
        print("Thanks for selecting Sedan cabs")
        print("The max speed that a Sedan cab go is 240 km per hour")
        print("The fair for per kilometer is rupees 22")
        self.km = 22 * self.km
        print("The total fair is: ", self.km)

class suv:

    def suv1(self, km):
        self.km = km
        print("Thanks for selecting Suv cabs")
        print("The max speed that a Suv cab go is 270 km per hour")
        print("The fair for per kilometer is rupees 25")
        self.km = 25 * self.km
        print("The total fair is: ", self.km)

class select(micro,mini,prime,sedan,suv):
    print("Welcome to OLA")

cab=select()
kms=float(input("Enter the number of kilometer: "))
choice=int(input("Enter the type of cab you need '\n'1.Micro '\n'2.mini '\n'3.prime '\n'4.sedan '\n'5.SUV '\n'"))

if (choice==1):
    cab.micro1(kms)
elif (choice==2):
    cab.mini1(kms)
elif (choice == 3):
    cab.prime1(kms)
elif (choice == 4):
    cab.sedan1(kms)
elif (choice == 5):
    cab.suv1(kms)
else:
    print("Wrong choice")