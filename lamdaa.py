def myfunc(n):
  return lambda a : a * n

a=int(input("enter value"))
n=int(input("enter value"))
mydoubler = myfunc(a)

print(mydoubler(n))
