l1 = ["python","java","php","flutter","android"]

l2 = list(map(lambda str : str.capitalize(),l1))\

print(l2)

l3 = list(map(str.capitalize,l1))
print(l3)