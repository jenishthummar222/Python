"""

List Comprehension with condition way 2

l2 = [value(left)  condition(right)  loop(center) ]

"""

# without Comprehension  

l1 = []

for i in range(1,10):
    if i%2!=0:
        l1.append("Odd")
    else:
        l1.append("Even")

print(l1)

#use Comprehension 

l2 = [(i,"Even") if i%2==0 else (i,"Odd") for i in range(1,10) ]
print(l2)