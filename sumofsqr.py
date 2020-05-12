#sum on squares first natural numbers
import math
a=int(input("enter a value"))
sum=0
for i in range(a+1):
    sum=sum+(math.pow(i,2))

print(sum)
