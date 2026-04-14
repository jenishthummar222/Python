for row in range(1,6):
    for col in range(1,6):
        print(" * ",end="")
    print()

print("-----------------")
for row in range(1,6):
    for col in range(1,6):
        if row==3 and col==3:
            print(" $ ",end="")
        else:
            print(" * ",end="")
    print()

print("-----------------")
for row in range(1,6):
    for col in range(row):
        print(" * ",end="")
    print()

print("-----------------")
for row in range(1,6):
    for col in range(row):
        print(f" {row} ",end="")
    print()

print("-----------------")
for row in range(1,6):
    for col in range(row):
        print(f" {col+1} ",end="")
    print()


print("-----------------")
k=5
for row in range(1,6):
    for col in range(1,6):
        if k>col:
            print(" ",end=" ")
        else:
            print(" * ",end=" ")
    print()
    k-=1

print("-----------------")
word = "INDIA"
for row in range(len(word)+1):
    for col in range(row):
        print(f"{word[col]} ",end="")
    print()
    