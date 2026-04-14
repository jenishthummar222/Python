student={
    'name':'jenish',
    'subject':'python',
    'score':90
}

print("\n-------- All --------")
for k,v in student.items():
    print(f"{k} = {v}")


print("\n-------- Keys --------")
for k in student.keys():
    print(f"{k}")

print("\n-------- Values --------")
for v in student.values():
    print(f"{v}")