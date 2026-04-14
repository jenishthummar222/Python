# remove()  / pop()

l1 = ["Python","java","c++","html","css","node.js"]

print(l1)

l1.remove("c++") # c++                         
print(l1)               #-> ['Python', 'java', 'html', 'css', 'node.js']

print(l1.pop()) # node.js    " => it's return remove element.  "   

print(l1)               #-> ['Python', 'java', 'html', 'css']

l1.pop(2) # html        
print(l1)               #-> ['Python', 'java', 'css']