# with map
l1 = [12,23,45,67,76,22]

def findEven(num):
    if num % 2 ==0:
        return num

l2 = list(map(findEven,l1))


#with filter()

def filterEven(num):
    if num%2 == 0:
        return num 

l3 = list(filter(filterEven,l1))

print(f"{l1}\n{l2}\n{l3}")