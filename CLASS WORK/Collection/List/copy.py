print("List 1")

l1 =[1,2,3]
print("l1 = ",l1)

l2 = l1       # pass references..

print("l2 = ",l2)

l2.remove(3)
print("l1 = ",l1)
print("l2 = ",l2)


print("List 2")
s1 = [4,5,6]

print("s1 = ",s1)
s2 = s1.copy()       # pass value..

print("s2 = ",s2)

s2.remove(4)
print("s1 = ",s1)
print("s2 = ",s2)