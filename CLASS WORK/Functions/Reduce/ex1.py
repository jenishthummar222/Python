"""
Reduce function is a similer like map and filter 

which is perform specific operation of each iterator and provide collection.

reduce your work.

"""

from functools import reduce 

l1 = [20,50,80,22,55,99]

obj = reduce(lambda a,b : a+b,l1)

print(obj)