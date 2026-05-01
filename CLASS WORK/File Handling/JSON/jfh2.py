# read data from the json file

import json

with open("JSON/myJsonFile.json","r") as f:
    data = json.load(f)

print(data)
print(data["name"])