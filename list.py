#all functions of list
newlist=[10,20,"hello",'g',[10,25,"hi"]]
print(newlist)
print(newlist[0])
#nested list
print(newlist[4][2])
#length of list
print(len(newlist))
#number of occurence in a list
print(newlist.count('g'))
#append
newlist.append(10)
print(newlist)
#reversing a list
list.reverse(newlist)
print(newlist)
#extend a list
newlist.extend('200')
print(newlist)
#removing a value from list
newlist.remove('0')
newlist.remove('0')
print(newlist)
#checking for a particular value in a list
if (10 in newlist):
    print("value exist")
#cloning
newlist2=newlist[:]
print(newlist2)
#inserting a value
newlist.insert(2,23)
print(newlist)
#delete
del newlist[5:8]
print(newlist)
#clear list
newlist.clear()
print(newlist)