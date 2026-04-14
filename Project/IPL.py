"""
                        IPL  2026 

            CSK   MI   GT  RR   RCB   KKR 


            Enter your team : CSK 

            opp. team : RCB 

    -------------------------------------
    TOSS TIME : 

            H/T 

            Enter your toss choice : H 

            actual toss coin : Head

            you won the toss chose bat for field 

    
    Enter your choice (bat/field) : field 

    ************   RCB  BATING FIRST ************

    SCORE BOARD :  RCB :  0/0  (0.0) overs 

    **********************************************

     (0 , 1 , 2 , 3 , 4 , 6 , "wide ball" , "no ball" , "wicket" )

            ********** IT's SIXER ***********
    
    SCORE BOARD :  RCB :  6/0  (0.1) overs 

            ********** 2 runs ***********
    
    SCORE BOARD :  RCB :  8/0  (0.2) overs 

            ********** NO BALL ***********
            ********** DOT BALL ***********
    SCORE BOARD :  RCB :  9/0  (0.2) overs

            ********** FREE HIT ***********

            ********** DOT BALL ***********
    SCORE BOARD :  RCB :  9/0  (0.3) overs

            ********** WICKET ***********

    SCORE BOARD :  RCB :  9/1  (0.4) overs        

            ********** WICKET ***********

    SCORE BOARD :  RCB :  9/2  (0.5) overs        


    CSK NEEDS 10 runs in 6 balls 
    
    ************   CSK  BATING ************
    
        ********** IT's SIXER ***********

    SCORE BOARD :  CSK :  6/0  (0.1) overs 

        ********** IT's a Boundary ***********

    SCORE BOARD :  CSK :  10/0  (0.2) overs 

            CSK WON THE MATCH !!


    hint : conditional , looping , variables , list , string ,random 

"""

import random

teams = ['GT','CSK','RCB','MI','KKR','RR','LSG','DC','SRH','PBKS']

print(f"""

                        IPL 2026 
""")
print("        ",end="")
for i in teams:
        print(i,end="  ")

opponent_tm =""

choice_tm = input("\n\n\tEnter Your Team :- ").upper()

if choice_tm in teams:                                       # -------------- team selection ----------------
        idx = teams.index(choice_tm)  
        auto_team = random.randint(0,9)
        
        if auto_team == idx and auto_team< len(teams)-1:
               
                opponent_tm = teams[auto_team+1]
                
        elif auto_team == idx and auto_team == len(teams)-1:
                opponent_tm = teams[auto_team-1]
                
        else:
                opponent_tm = teams[auto_team]
        
        print("\tOpponent Team Is :- ",opponent_tm)

        print("""\n\t-------------------------------------                  
        TOSS TIME : 

                        H/T
             """ )                                              #  -------------- Toss ---------------- 
        toss = input("\tEnter Your Choise :- ")[0].upper()
        coin = random.choice(["Head","Tail"])
        print(f"\tactual toss coin :- {coin}\n")
        print("\t-------------------------------------\n")
        choice=""
        batting_team,bowling_team = None,None
        if toss == coin[0] :
                print(f"\t{choice_tm} won the toss choice bat or field ")
                choice = input("\tEnter your choice (BAT/FIELD) : ")[0].upper()

                if choice=="B":
                        batting_team = choice_tm
                        bowling_team = opponent_tm                        
                else:
                        batting_team = opponent_tm
                        bowling_team = choice_tm
                        
        else:
                choice = random.choice(["BAT","FIELD"])
                print(f"\t{opponent_tm} won the toss & Choice {choice} ")

                if choice=="FIELD":                        
                        batting_team = choice_tm
                        bowling_team = opponent_tm                        
                else:
                        batting_team = opponent_tm
                        bowling_team = choice_tm
                        
        print(f"\n\t==============   {batting_team}  BATING FIRST ============== ") #  -------------- Match Start ---------------- 
        input()

        sorts = [0 , 1 , 2 , 3 , 4 , 6 , "wide ball" , "No ball" , "wicket" ]  

        number,score,team1_score= 0,0,0

        while number <2:

                print("\t********  Match Start ********\n")

               # print(f"\n\tSCORE BOARD :  {batting_team} :  0/0  (0.0) overs\n")             

                wicket,ball,freehit = 0,0,False

                while ball < 6 and wicket < 2: 
                        
                        if number == 1:
                                if team1_score - score <0 :
                                        break
                        
                        print(f"\t{ball+1} Ball...")
                        input()

                        hit = random.choice(sorts)   
                                        
                        match hit:
                                case 0:
                                        print("\t\t. DOT BALL .")
                                        freehit = False
                                
                                case 1:
                                        print("\t\t* 1 RUN *")
                                        score+=1
                                        freehit = False
                                        
                                case 2:
                                        print("\t\t** 2 RUN **")
                                        score += 2
                                        freehit = False
                                        
                                case 3:
                                        print("\t\t*** 3 RUN ***")
                                        score += 3
                                        freehit = False
                                        
                                case 4:
                                        print("\t\t**** 4 RUN ****")
                                        score += 4
                                        freehit = False
                                                
                                case 6:
                                        print("\t   ****** IT's MAXIMUM ******")
                                        score += 6
                                        freehit = False
                                        
                                case "wide ball":
                                        print("\t~~~~~~~~~~ Wide Ball ~~~~~~~~~~~~~")
                                        score += 1  
                                        print(f"\n\tSCORE BOARD :  {batting_team} :  {score}/{wicket}  (0.{ball}) overs")
                                        input()
                                        continue                             
                                
                                case "No ball":
                                        sorts = [0 , 1 , 2 , 3 , 4 , 6 ,"wicket" ]
                                        hit = random.choice(sorts)
                                        match hit:
                                                case "wicket":
                                                        print("\t********** Run Out + No Ball ***********")
                                                        wicket += 1 
                                                        print(f"\n\tSCORE BOARD :  {batting_team} :  {score}/{wicket}  (0.{ball}) overs\n")
                                                case _:
                                                        score += hit

                                                        print(f"\t^^^^^^^^^ {hit} + No Ball ^^^^^^^^^ ")
                                                        score += 1 
                                                        print(f"\n\tSCORE BOARD :  {batting_team} :  {score}/{wicket} (0.{ball}) overs \n")
                                        if wicket < 2 :
                                                print("\t@@@@@@@@@@@ Free Hit @@@@@@@@@@@@")   
                                                freehit = True
                                                input()

                                        continue

                                case "wicket":
                                        if freehit :
                                                print("\t********** Wicket :- Run Out ***********")
                                                freehit = False
                                        else:
                                                out = random.choice(["Bowled","Catch Out","Run Out"])
                                                print(f"\t********** Wicket :- {out} ***********")
                                                freehit = False
                                        wicket += 1                                                   

                        print(f"\n\tSCORE BOARD :  {batting_team} :  {score}/{wicket}  (0.{ball}) overs\n")
                        ball += 1   
                        input()             

                print("\t==========================================")                
                
                if number == 1: 
                        
                        if score == team1_score:
                                print("\n\tMatch Tie.. Let's Play Another One..\n")
                                print("\t==========================================") 
                                print(f"\n\t{batting_team} Start's First")
                                score = 0
                                number = 0
                                input()
                        elif score < team1_score:
                                print(f"\n\t\t☆ {bowling_team} ☆ WON THE MATCH !!\n")
                                print("\t☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆\n")
                                number += 1     
                        else:
                                print(f"\n\t\t☆ {batting_team} ☆ WON THE MATCH !!\n")
                                print("\t☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆\n")
                                number += 1    
                else:
                        print(f"\n\t\t{bowling_team} Need {score+1} in 6 Ball\n")

                        print("\t==========================================\n") 

                        temp = batting_team   
                        batting_team = bowling_team
                        bowling_team = temp     

                        team1_score = score 
                        score = 0 
                        number += 1     

else:
        print("\tTeam Not Exists..")

