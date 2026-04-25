def myDcorators(myfun):                         # accept function as args.
    def Wrapper():                              # wrapp a actual function before or after function 
        print("Alarm .. 5:00 ...")
        print("Alarm .. 6:00 ...")
        myfun()                                 # calling actual function
        print("getting ready for office..")
    return Wrapper

@myDcorators                                    # this is sysntax for decorator function
def sayHello():
    print("Good Morning..")


sayHello()                                      # call actual function automatic call decorator function.