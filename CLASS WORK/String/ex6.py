# strip()  -> remove whitespace  || lstrip() || rstrip()

s1 = " My  Python         "

print(len(s1),"Full Length")

s2 = s1.strip()

print(len(s2),"Remove All Space")

s3 = s1.lstrip()

print(len(s3),"Left Space Remove")

s4 = s1.rstrip()
print(len(s4),"Right Space Remove")