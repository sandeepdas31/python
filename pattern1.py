n= int(input("the type lines of pattern you want to print :"))

for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print('\r')


