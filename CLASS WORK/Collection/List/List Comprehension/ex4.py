l1 = ["java","python","rectjs","php","flutter"]

print(l1)

#without list comprehension

l2 =[]

for name in l1:
    if len(name )>4:
        l2.append(name)

print(l2)

#using list comprehension

l3 = [name for name in l1 if len(name)>4]
print(l3)

