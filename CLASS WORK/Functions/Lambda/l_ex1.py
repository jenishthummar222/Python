"""
    Lambda function :- it function is an anonymus function

"""

# without lambda

def myfun(num):
    return num*num

print(myfun(5))


#with lambda

ans = lambda num: num * num 
print(ans(10))