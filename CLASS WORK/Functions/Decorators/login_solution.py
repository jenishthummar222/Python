# solution.
data = {
    "email" : "a@gmail.com",
    "password" : "123456",
    "username":"jenish",
    "check_login":False
}

def login():
    email = input("Enter Email :- ")
    password = input("Enter Passeword :- ")

    if email == data["email"] and password == data["password"]:
        data["check_login"]= True
        print("suncessfully Login..")
    else:
        print("Invalid Data")

def checkLogin(myfun):
    def wrapper():
        if data["check_login"] == True:
            myfun()
        else:
            print("You Are not Login..")
    return wrapper

@checkLogin
def dashboard():
    print("Welcome to DashBoard")


@checkLogin
def profile():
    print("Welcome to Profile")

@checkLogin
def logout():
    data["check_login"] = False
    print("You are Logout..")

while True:
    print("""
            Menu
    ------------------------
            1: login
            2: dashbord
            3: profile
            4: logout
            5: Exit
    
    """)
    choice = int(input("Enter Your Choice :- "))
    if choice == 1:
        login()
    elif choice == 2:
        dashboard()
    elif choice==3:
        profile()
    elif choice==4:
        logout()
    else:
        break


