def maxmin(x):
    big=x[0]
    small=x[0]
    for i in range(len(x)):
        if(x[i]>big):
            big=x[i]
        if(x[i]<small):
            small=x[i]
    print("the big number in the list is", big)
    print("the small number in the list is", small)

number= int(input("enter the total values in a list: "))
a=[]
for i in range(1,number+1):
 print("enter value ",i, ": ", end="" )
 a.append(input())
print(a)
maxmin(a)

