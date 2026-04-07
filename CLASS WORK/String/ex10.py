
s1 = "pYtHOn"

s2 = ""

for char in s1:
    if char.isupper():
        s2+= char.lower()
    else:
        s2 += char.upper()

print(f"{s1}\n{s2}")
