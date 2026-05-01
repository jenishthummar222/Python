def findFactorial(num):
    f = 1
    for i in range(2,num+1):
        f *= i 
    return f

def checkEvenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
