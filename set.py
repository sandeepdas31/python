#unique values
newset={10,20,10,"hello"}
print(newset)
#adding values in set
newset.add(500)
print(newset)
newset.update([500,200,500])
print(newset)
#deleting values
newset.discard(200)
print(newset)
newset.remove(10)
print(newset)
#set operations
#union
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a.union(b))
print(b.union(a))
print(a|b)
#intersection
print(a.intersection(b))
print(a&b)
#set difference
print(a-b)
print(b-a)
print(a^b)
