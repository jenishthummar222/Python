u_email = "a@gmail.com"
u_password = "123"
userName = "Admin"

menu = """ 

            MENU
        press 1: Login
        press 2: Register
        press 3: Exit
"""

status = True

while status:

    print(menu)

    choice = int(input("Enyet Your Number :- "))

    match choice:
        case 1:
            print("LOGIN")
            email = input("Enter Your Email :- ")
            password = input("Enter Your Password :- ")

            if email==u_email and password == u_password:
                print(f"Welcome {userName}")
            else:
                print("Invalid Password OR Email..")

        case 2:

            print("REGISTER")

        case 3:
            print("Thank You..")
            status=False