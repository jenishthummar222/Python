"""
when we work with file we have to close it manually 

if we forgot to close file there are posibility to loss data or error chances.

to resole this issue we have one concept manager which called "With"

using of with it automatically handle file closing operation.
"""

with open("file.txt","r") as f:
    print(f.read())
