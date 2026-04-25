"""
    ~> os module which is represent as an operating system.
    ~> which is mainly use to programaticallly access os path, folder,files and many more.
    ~> using of program and scripting we can control os program.


"""


import os


print("my current working directory ::: ",os.getcwd())

"""
    ~> getcwed() ::-
            -> get current working directory
"""

print("\n-------os.listdir()--------")

print(os.listdir())

count = len(os.listdir())

print("Total File Or Folder are ::- ",count)

print("\n-------chdir()----------")

print("Change Directory ::- ")
os.chdir(os.getcwd()+"\\CLASS WORK")
print(os.getcwd())
print(os.listdir())


# mkdir() :- when we want to create directory.
print("\n-------mkdir()----------")
print("Make Directory ::-")
print(os.getcwd())
os.mkdir("Hello")
print("successfukky..")

# makedirs() :- create multiple directorys nested directory.. 
os.makedirs("hi/five/hello/bhai")
#------------------------------------------------------------------
print("\n-------rmdir()----------")

print("Remove single Directory..")
os.rmdir("Hello")
print("Remove Nested Directory ")
os.removedirs("hi/five/hello/bhai")







