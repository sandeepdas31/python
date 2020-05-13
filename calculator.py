#calculator program

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

a=float (input("enter one value"))

b=float (input("enter another value"))

print("select an option '\n'1.add '\n'2.sub '\n'3.mul '\n'4.div")

choice=str (input("enter a choice"))

if choice == "1":
    print("addition:", add(a,b))

elif choice=='2':
    print("subtraction:", sub(a,b))

elif choice=='3':
    print("multiplication:", mul(a,b))

elif choice=='4':
    print("division:", div(a,b))

else:
    print("wrong choice selected")
    

