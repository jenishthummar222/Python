# accept 5 number from user and check enter number is positive or nagative. 

num = 0
for i in range(1,6):
    num = int(input(f"Enter Your {i} Number :- ")) 

    if num > 0: 
        print(f"{num} is Positive.")
    else:
        print(f"{num} is Nagative.")

    print("Positive " if num > 0 else "Nagetive")