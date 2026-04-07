import random

print("************************* Number Guessing Game *****************************")

level = """ 
            Press 1: Level 1
            Press 2: Level 2
            Press 3: Level 3
        """

print("Desripion :: Guess Number between 1 to 100")

#Generate Number Between 1 to 100

computer = random.randint(1,100)

status = True
limit = 1

print(level)

lvl = int(input("ENter Your Level :- "))
match lvl:
    case 1:
        while status :

            user = int(input("Enter Your gussing Number :- "))

            if user > computer:
                print("HINT : Guess Lower Number.")
            
            elif user < computer:
                print("HINT : Guess Uper NUmber.")
                
            else:
                print("Right Guess..")
                status=False
    case 2:
        print("Guess Number Before Limit 5 ")
        status = True
        while limit <= 6 and status :
            
            if(limit < 5):
                user = int(input("Enter Your gussing Number :- "))      
                
            else:

                user = int(input("Enter Your gussing Number :- "))
        
                print("This Is Your Last Chance ")

            
            if user > computer:
                if limit < 6:
                    
                    print(f"HINT : Guess Lower Number.")

                    limit += 1
                else:
                    print("Game Over")
            
            elif user < computer:
                if limit < 6:
                    print(f"HINT : Guess Uper Number.")
                    limit += 1
                else:
                    print("Game Over")
                
            else:
                print("Right Guess..")
                status=False
                