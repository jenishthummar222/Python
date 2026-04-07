# Accept 5number from user check Enter number is positive or nagetive and count total positive and nagative.


positive = 0
nagetive = 0
for i in range(1,6):
    num = int(input(f"Enter Your {i} Number :- ")) 

    if num>0:
        positive +=1
    else:
        nagetive +=1

print(f"Total Positive Number Is {positive}")
print(f"Total Positive Number Is {nagetive}")