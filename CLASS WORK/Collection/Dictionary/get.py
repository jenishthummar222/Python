student={
    'name':'jenish',
    'subject':'python',
    'score':90
}

# acess dictionary
print(student['name'])

print(student['score'])


#print(student['city'])  # it's throw error  KeyError: 'city'

#access dictionary


print(student.get('name'))

print(student.get('score'))

print(student.get('city'))      # it's print none value or defualt value if you given
print(student.get('city',"Ahmedabad")) 