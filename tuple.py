newtuple=(10,2.0,"hello",(25,'hi'))
print(newtuple)
#fetching a item
print(newtuple[0])
#adding a value
newlist=list(newtuple)
newlist.append(10)
newtuple=tuple(newlist)
print(newtuple)
#printing all values in a tuple
for x in newtuple:
    print(x)
#reverse indexing
print(newtuple[-1])
#length of tuple
print(len(newtuple))
#type of tuple
tuple1=("ap",)
print(type(tuple1))
#unpacking
tuple2= 3,2.0,"h2llo"
print(tuple2)
a,b,c= tuple2
print(a)
print(b)
print(c)
print(type(tuple2))

tuple2=34
print(tuple2)