# Kon Banega Carodpati 

import random


KBC = {
    1:
    {    
       """What is the output of this code?
        print(type([]))
        """:
           [
            "A) <class 'list'>",
            "B) <class 'tuple'>",
            "C) <class 'dict'>",
            "D) <class 'set'>"
            ],
        1:"A"

    },
    2:
    {
        "Which of the following is immutable?":
        [ 
            "A) List",
            "B) Dictionary",
            "C) Tuple",
            "D) Set"
        ],
        2:"C"

    },
    3:
    {
        """What will this code print?
        x = [1, 2, 3]
        print(x * 2)
        """:        
        [ 
            "A) [2, 4, 6]",
            "B) [1, 2, 3, 1, 2, 3]",
            "C) Error",
            "D) [1, 4, 9]"
        ],
        3:"B"
    }
    
}

life_line = {"Ask Friend":True,"Remove 2 Wrong":True} 

total_que = 3
total_amt = (10000000/total_que)
question = random.sample(range(1,len(KBC)+1),total_que)
balance = 0


def getQuestions_And_Answer(number):
    for qu in KBC[number].keys():
        if qu != number:
            print(f"\n{qu}\n")
            for opt in KBC[number][qu]:
                print(opt)
        else:
            return KBC[number][qu]

def ask_friend(current_ans,name):
    print("\nThis is Ask Friend Life Line ...")
    input("\nPress Enter For know your friend's answer..")
    print(f"\nYour Friend Say Answer is.. {current_ans} ")
    life_line[name] = False
    return input("\nEnter Your Answer :- ").upper()

def check_answer(answer,set_answer):
    if answer == set_answer:
        print("\nCongratulation ....Your Answer is Right ..")
        return True
    else:
        print("\nThat's The WRONG Answer.")
        return False

def player_balance(check_ans,balance):
    if check_ans:
        balance += total_amt
    else:
        balance -= (total_amt/2)

    return 0 if balance <0 else balance


lf= 1
print(f"""
-------------------------------------------------------
                    Welcome To KBC
-------------------------------------------------------
    Rule :~
            A. Total Question is {total_que}.
            B. You have Only {len(life_line)} life line. """,end="")
for lfl in life_line.keys():
    print(f"{lf} :- |{lfl}| ",end=" ")
    lf += 1
    
print(f"""
            C. Per question, you get ₹{(total_amt):.2f} for each correct answer.
            D. For a wrong answer, ₹{(total_amt//2):.2f} will be deducted from your current balance.
            E. Total prize pool is ₹1 Cr.

""")
input("Press Enter To Start ...")

for i in question:
    set_answer = getQuestions_And_Answer(i)
    while True:
        use_answer = input("\nEnter Your Option  :: \nL : Life Line\nA to D : Answer ==> ").upper()

        match use_answer:
            case "L":
                id = 1
                print("\n")
                counter = 0
                for lfln in life_line.keys():
                    if life_line[lfln] == True:
                        print(f"{id} :-| {lfln} |",end=" ")
                    else:
                        counter += 1
                    id +=1
                if counter != len(life_line):

                    while True:
                        lifeLine = int(input("\n\nEnter Your Life Line Number :- "))
                        match lifeLine:
                            case 1:
                                ans = check_answer(ask_friend(set_answer,list(life_line.keys())[lifeLine-1]),set_answer)
                                balance = player_balance(ans,balance)
                                
                                break
                            case 2:
                                pass 
                                break
                            case _:
                                print("\n There is no such option.")
                else:
                    print()
                break
            case "A"|"B"|"C"|"D":
                ans = check_answer(use_answer,set_answer)
                balance = player_balance(ans,balance)
                
                break
            case _:                
                print("\n There is no such option..")
    print(f"""
-------------------------------------------------------
            Balance :- {balance:.2f}
-------------------------------------------------------""")        
    if i != total_que:    
        input("\n\tPress Enter ..Next..")
    else:
        print("Thank you !! for Play..")

    