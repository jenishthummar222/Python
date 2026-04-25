l1 =["mom","world","nayan","india"]

l2 = list(map(lambda st:st[::-1],l1))
print(l1)
print(l2)

l3 = list(filter(lambda st:st[::-1] == st,l1))
print(l3)

l4 = list(filter(lambda st:st[::-1] == st,map(lambda st:st[::-1],l1)))
print(l4)