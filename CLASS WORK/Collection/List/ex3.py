"""
    Inbuilt Functions And Methods of List
"""

l1 = [54,22,7,9,73,4,52,31,89]

print(f"Length of List {len(l1)}")

print(f"Max Element from List {max(l1)}")
print(f"Min Element from List {min(l1)}")
print(f"Addition of all Element {sum(l1)}")

l1.reverse()
print(l1)

l1.sort()  # defualt sort ascending order
print(l1)

l1.sort(reverse=True)  # sort descending order
print(l1)