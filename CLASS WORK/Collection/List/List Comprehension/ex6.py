l1 = ["python","java","php","Flutter","Android"]

l2 =[]

# without list comprihension.

for word in l1:
    if word[::-1]==word:
        l2.append("Palindrom")
    else:
        l2.append("Not Palindrom")

# with list comprihension.

l3 = [[word,"palindrom"] if word[::-1]==word else [word,"not a palindrom"] for word in l1]

print(l1)

print(l2)

print(l3)