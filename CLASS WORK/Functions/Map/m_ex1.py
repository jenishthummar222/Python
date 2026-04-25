# without MAp 

l1 = [10,20,30,40,50]

l2 = []

for i in l1:
    l2.append(i +5)

print(l1)
print(l2)


#with Map

l2 = list(map(lambda num: num+5 , l1))

print(l2)