def myDecorator(myfun):             # if you not create function inside decorator it's not work properly if you use multiple time. 
    
    print("Before") 
    myfun()
    print("After")
    return myfun()


@myDecorator
def sayHello():
    print("hello")

sayHello
sayHello