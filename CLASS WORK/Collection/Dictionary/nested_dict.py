quize = {
    1:{
        'que':"Who is prime Minister of India ?",
        'ans':'narendra modi'
    },
    2:{
        'que':"Most Popular Programing Language ?",
        'ans':"python"
    },
    3:{
        'que':"First Fasted 50 run Player ?",
        'ans':"uvraj shing"
    }
}

#print(quize)
#print(quize[1][que])

score = 0
for i in range(len(quize)):
    print(f"Quize ({i+1}) :- {quize[i+1]['que']}")
    ans = input("Enter Your Answer :- ").lower()

    if ans == quize[i+1]['ans']:
        print("Right Answer")
        score += 1
    else:
        print("Wrong Answer")

print(f"Your Score is : {score}")

