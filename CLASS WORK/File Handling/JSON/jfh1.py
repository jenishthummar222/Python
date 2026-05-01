"""
JSON :- javascript object notation

python contain complex data type when we want to send that data to js developer or any frontend developer.

but at that time javascript developer or frontend developer dose not understand complex prgraming code at that 
time convert our code to json universal language.

json convert object data into string 

"""
import json 
data = {
    "id":1,
    "name":"Giyan",
    "subject":"python"
}

print("Python data :",data)

with open("myJasonFile.json","w") as f:
    json.dump(data,f,indent=4)

print("File Created successfully...")