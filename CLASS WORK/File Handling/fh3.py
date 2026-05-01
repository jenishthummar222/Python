f = open("file.txt","r")

data = f.readlines()            # fetch all line from the file.

print(data)

print("no. of lines : ",len(data))

f.close()