"""
  get temperature value from user 

"""
# 1st way
hotdays_list =[]
"""
for i in range(6):
    date = input("Enter Date :- ")
    temp = float(input("Enter Temperature :- "))

    if temp > 25:
        hotdays_list.extend([date,temp])

index = 0 
for i in hotdays_list:
    if index % 2 ==0:
        print(f"{i} temp is",end=" ")
    else:
        print(f"{i}")
    index+=1
"""
# 2 way

for i in range(6):
    date = input("Enter Date :- ")
    temp = float(input("Enter Temperature :- "))

    if temp > 25:
        result = f"{date} temp is {temp}"
        hotdays_list.append(result)
    
for i in hotdays_list:
    print(i)