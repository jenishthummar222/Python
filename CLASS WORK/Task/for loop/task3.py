# accept 5 numbers from user and perform addition operation.

sum = 0
for i in range(1,6):
    num = int(input(f"Enter your {i} Number :- "))
    sum += num

print(f"Sum is {sum}") 

