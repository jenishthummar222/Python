# positional args & keyword args 

def student(name,score):
    print(f"name = {name}")
    print(f"score = {score}")


#Positional Args 
student("AAA",89)

# student(89,"AAA")   => get wrong answer

#keyword Args
student(name="ram",score=89)

student(score=89,name="ram")