""" 
    Bank Managment System

"""

user_Info = {
    'dummy@gmail.com':{
        'name':"dummy",
        'account_no':1001,
        'password' : '123'
    }
}

bank_Accounts = {
    1001:{
        "Balance":5000,
        "Taransactions":{
            "withdraw":0,
            "deposite":0
        }
    }
}

welcome = ("""
            WELCOME To BANK
    ------------------------------
        1: Create Account..
        2: Login Account..
        3: Exit

""")
accountNo = 1001
while True:
    print(welcome)
    press = int(input("Enter Your Choice : "))

    if press == 1:
        print("""
                    Create Account Page
            --------------------------------------            
        """)
        Emial = input("Enter Your Email :- ")
        if Emial not in user_Info:

            name = input("Enter Your Name :- ")
            password = input("Enter Your Password :- ")
            accountNo += 1
            opaning = float(input("Enter your opaning Account Balance [min : 5000] :- "))

            if opaning >= 5000:
                print("Your Account is Open..")
                user_Info[Emial] = {
                    'name':name,
                    'account_no':accountNo,
                    'password' : password
                }
                bank_Accounts[accountNo] = {
                    "Balance":opaning,
                    "Taransactions":
                        {
                            "withdraw":0,
                            "deposite":0
                        }
                }

                print(f"""
                            Account Details
                    ------------------------------
                        name :- {user_Info[Emial]['name']}
                        Account No :- {user_Info[Emial]['account_no']}
                        Balance :- {bank_Accounts[accountNo]['Balance']}
                """)

            else:
                print("Don't allow minimum Opaning Account Balance.. Recreate Account")



        else:
            print("\nYour Email is Already Exists..")
        pass 
    elif press == 2:
        print("""
                    Login Into Account 
            --------------------------------------            
        """)
        Emial = input("Enter Your Email :- ")
        password = input("Enter Your Password :- ")
        
        if Emial in user_Info:
            if password == user_Info[Emial]['password']:
                while True:
                    print(f"""\n
                        Welcome Back {user_Info[Emial]['name'] }..
                --------------------------------------
                        1 : withdraw 
                        2 : Deposite
                        3 : Check Balance
                        4 : Transaction
                        5 : Exit

                    """) 

                    select = int(input("Enter Your Option :- "))

                    if select == 1:
                        withdrow_Amount = float(input("Enter Your Withdrowal Amount :- "))

                        if  bank_Accounts[user_Info[Emial]['account_no']]['Balance'] >= withdrow_Amount:
                            bank_Accounts[user_Info[Emial]['account_no']]['Balance'] -= withdrow_Amount
                            bank_Accounts[user_Info[Emial]['account_no']]['Taransactions']["withdraw"] += withdrow_Amount 
                            print("\n Withdrow Successfully....")
                            print(f"\nYour Total Balance Is :- {bank_Accounts[user_Info[Emial]['account_no']]['Balance']}")                             
                        else:
                            print("insufficient balance.. Retry..")



                    elif select == 2:
                        
                        deposite_amount = float(input("Enter Your Deposite Amount :- "))
                        bank_Accounts[user_Info[Emial]['account_no']]['Balance'] += deposite_amount
                        bank_Accounts[user_Info[Emial]['account_no']]['Taransactions']["deposite"] += deposite_amount
                        print("\n Deposite Successfully....")
                        print(f"\nYour Total Balance Is :- {bank_Accounts[user_Info[Emial]['account_no']]['Balance']}")   
                         
                    elif select == 3:
                        print(f"\nYour Total Balance Is :- {bank_Accounts[user_Info[Emial]['account_no']]['Balance']}") 

                    elif select == 4:
                        print(f"""
                        Transaction history 
                -------------------------------
                        Deposite: {bank_Accounts[user_Info[Emial]['account_no']]['Taransactions']['deposite']}
                        Withdraw: {bank_Accounts[user_Info[Emial]['account_no']]['Taransactions']['withdraw']}

                        """) 
                    else :
                        break
            else:
                print("Your Password is Wrong.. ")
        else:
            print("Your Email is not Exists..")
    else:
        break