data = {
    "email" : "a@gmail.com",
    "password" : "123456",
    "username":"jenish"
}

def login():
    email = input("Enter Email :- ")
    password = input("Enter Passeword :- ")

    if email == data[email] and password == data[password]:
        print("suncessfully Login..")
    else:
        print("Invalid Data")

def dashboard():
    login()
    print("Welcome to DashBoard")

def profile():
    email = input("Enter Email :- ")
    password = input("Enter Passeword :- ")

    if email == data["email"] and password == data["password"]:
        print("suncessfully Login..")
    else:
        print("Invalid Data")
    print("Welcome to Profile")

while True:
    print("""
            1: login
            2: dashbord
            3: profile
            4: exit
    
    
    """)
    choice = int(input("Enter Your Choice :- "))
    if choice == 1:
        login()
    elif choice == 2:
        dashboard()
    elif choice==3:
        profile()
    else:
        br

"""
Note :- 
    proble :-
        if you go another page all time to check if user login or not and code is so long . that's why use decorators.
"""
