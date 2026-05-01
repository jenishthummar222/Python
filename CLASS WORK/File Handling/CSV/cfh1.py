# csv :- comma seperated value. 

import csv 
data = [
    ["Sr.No","NAME","SUBJECT"],
    [1,"aaa","python"],
    [2,"bbb","java"],
    [3,"ccc","PHp"]
]

with open("CSV/myCSVFile.csv","w",newline="") as f:
    # create write object of csv
    write = csv.writer(f)

    write.writerows(data)

print("File Created...")
