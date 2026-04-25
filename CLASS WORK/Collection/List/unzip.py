"""

    unzip =:
        ~> it is a opposits of zip function.
        ~> zip which is used to marge or combine multiple list into single object.
        ~> unzip is used to split zipped into seperated variable.
        ~> there is no keyword as unzip.
        ~> use * for unzip.

"""



l1 = ["java","python","php","c++"]
marks= [90,80,95,96]

l2 = list(zip(l1,marks))

print(l2)

key,value = zip(*l2)

print(key)
print(value)