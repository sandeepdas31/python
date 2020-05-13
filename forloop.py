#code to run addition program in loop
def add(x,y):
    return x+y

x= int(input("print the number of times you want to run the add loop"))

for X in range(x):
    a= float(input("enter a variable"))
    b= float(input("enter another variable"))
    print("addition: ", add(a,b))
