l1 = ["java","python","android","php","flutter"]

l2 =[]

for sub in l1[::-1]:
    l2.append(sub[::-1])


print(l1)
print(l2)