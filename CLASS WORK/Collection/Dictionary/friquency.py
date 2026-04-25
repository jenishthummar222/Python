# find charector friquency and store in dictionary.abs

d = {}

name = input("Enter Your Name : ")

for char in name:
    if char in d.keys():
        d[char] = d[char]+1 
    else:
        d[char] = 1

print(d)