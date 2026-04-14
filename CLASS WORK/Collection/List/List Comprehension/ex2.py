"""

List Comprehension with condition

l1 = [value(left)  loop(center)  condition(right)]


"""

# without Comprehension  odd  number

l1 = []

for i in range(1,10):
    if i%2!=0:
        l1.append(i)

print(l1)

#use Comprehension even number

l2 = [i for i in range(1,10) if i%2==0]
print(l2)