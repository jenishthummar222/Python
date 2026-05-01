import json 

user = []

no = int(input("Enter How Many User  :- "))

for i in range(no):
    obj = {}

    obj["name"]=input("Enter User Name :- ")
    obj["Subject"] = input("Enter Subject Name :-")
    obj["Score"] = int(input("Enter Score :- "))

    user.append(obj)

with open("JSON/JsonFile.json","w") as f:
    json.dump(user,f,indent=4)

print("Data added Successfully..")