marks = int(input("Enter your marks :- "))

if marks>=0 and marks<=100:
    
    if marks<=100 and marks > 90:
        print("Grade A")
    elif marks<=90 and marks > 80:
        print("Grade B")
    elif marks<=80 and marks > 70:
        print("Grade C")
    elif marks<=70 and marks > 60:
        print("Grade D")
    else:
        print("Fail")
        
else:
    print("Invalid Marks")