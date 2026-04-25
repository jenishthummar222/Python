l1 = [12,2,32,22,42,52]

def myfun(num):
    if num%2 == 0:
        return f"{num} = Even"
    else:
        return f"{num} = Odd"

    
l2 = list(map(myfun,l1))

print(l2)