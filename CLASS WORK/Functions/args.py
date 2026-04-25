# *args  :- arguments :- tuple as a parameters. 
# **kargs : key with arguments :- dictinory as a parameters. 

def myFun(*args):
    for i in args:
        print(i)

myFun(10,50,60,80,70,90.20)



