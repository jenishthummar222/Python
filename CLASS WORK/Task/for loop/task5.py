# Accept 4 number from user And check ENter number Even or odd.

for i in range(4):

    num = int(input(f"Enter Your {i+1} Number :- "))

    print("Even" if num%2 ==0 else "Odd")