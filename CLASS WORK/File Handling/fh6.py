# accept name from user and save in file.

file = open("UserName.txt","w")

for i in range(5):
    name = input("Enter Your Name : ")
    file.write(f"Name :- {name}\n")

file.close()