"""
    l1 = ["java","python","php","c++"]
    marks= [90,80,95,96,60]                 # 60 have not pair.

    l2 = list(zip(l1,marks))

    print(l2)

    OUTPUT

        [('java', 90), ('python', 80), ('php', 95), ('c++', 96)]

    Notr :-
        ~> if pair is'n meet ,it not take by zip() function.

"""


l1 = ["java","python","php","c++"]
marks= [90,80,95,96]

l2 = list(zip(l1,marks))

print(l2)