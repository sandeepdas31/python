def gcd(x,y):
    for z in range(2,x+1):
        flag=0
        if x%z==0 and y%z==0:
            gcd=z
            flag=1

    if flag==1:
        print("the gcd for the numbers", x, y, "are", z)
    if flag==0:
        print("there is no gcd for",x,y)

a= int(input("enter a value"))
b= int(input("enter another value"))
gcd(a,b)