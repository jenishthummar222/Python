#function with pra and wihthout return type

def findFactorial(num):
    f = 1
    for i in range(1,num+1):
        f *= i

    print("Factorial : ",f)

findFactorial(5)