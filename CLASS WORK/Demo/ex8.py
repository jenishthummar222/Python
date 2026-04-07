""" Format Function or Format string """

num = int(input("Enter Number : "))
name = input("Enter Name : ")

"""
    -> expected output : your name is ______ and your num is _____.
"""
print("your name is",name,"your num is",num)

print(f"your name is {name} your num is {num}")

n1=int(input("Enter Number 1 : "))
n2=int(input("Enter Number 2 : "))

ans = n1 + n2

print("Using format String")
print(f"{n1} + {n2} = {ans}")

print("Using Format Function ")
print("{2} = {0} + {1} ".format(n1,n2,ans))

# ======================================================================================

"""     
    -> My name is ________ i am _________ years old.
    -> My main Technology is _________ , This ___________ technology is most popular and my score is ___.    
    
"""

name = input("Enter your name :- ")
age= int(input("Enter your Age :- "))

technology = input("Enter your Technology :- ")
score = int(input("Enter your score :- "))

print(f"My name is {name}, i am {age} year old.")
print(f"My main Technology is {technology} , This {technology} technology is most popular and my score is {score}")