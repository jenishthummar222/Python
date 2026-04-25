data = {}

def registration():
    email = input("Enter Your Email :- ")
    if email in data.keys():
        return "Already Exists..!"
    
    name = input("Enter your name :- ")
    password = input("Enter your password :- ")

    data[email] = {
        "name": name,
        "password":password
    }
    return "Successfully Registered !!"

def login():
    email = input("Enter your Email :- ")
    password = input("Enter your Password :- ")

    if email in data.keys():
        if data[email]["password"] == password:
            return f"Welcome {data[email]["name"]}"
        else:
            return "Invalid Login Password.."
    else:
        return "Invalid Email.."

menu = """
            Menu
    --------------------
    1:  Registration
    2:  Login
    3:  Exit
"""

while True:
    print(menu)

    select = int(input("Enter your choice :- "))

    if select == 1:
        print(registration())
    elif select == 2:
        print(login()) 
    else:
        break