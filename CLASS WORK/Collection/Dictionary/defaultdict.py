from collections import defaultdict

d = defaultdict(int)

list = ["java","python","java","c++","php","python","java"]

for word in list:
    d[word] = d[word]+1

print(d)