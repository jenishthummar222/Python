""" accept 5 students name and score 

    check if student's score is more than 70 

    just print list of studennt names.

"""
name_list =[]

for i in range(5):
    name = input("Enter Your Name :- ")
    score = int(input("Enter Your Score :- "))

    if score > 70 :
        name_list.append(name)
    
print("List Of Student Whos Score is above 70+ :- ",name_list)

