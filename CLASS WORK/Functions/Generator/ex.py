# def myfun():
#     return 1
#     return 2
#     return 3

#but using generator (yield)

def myGenerator():
    yield 1
    yield 2
    yield 3

obj = myGenerator()

print(next(obj))        # 1
print(next(obj))        # 2
print(next(obj))        # 3
print(next(obj))        # getting error
