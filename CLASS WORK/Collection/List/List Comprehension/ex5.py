l1 = ["python","java","php","Flutter","Android"]

l2 =[]

# without list comprihension.

for sub in l1:
    l2.append(sub[:3])

print(l1)
print(l2)

# with list comprihension.

l3=[sub[:3] for sub in l1]

print(l3)

