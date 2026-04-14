even_li =[]
odd_li =[]

for i in range(5):
    val = int(input("Enter Your Number :- "))

    if val % 2 == 0:
        even_li.append(val)
    else:
        odd_li.append(val)
    
print("Even List :- ",even_li)

print("Odd List :- ",odd_li)