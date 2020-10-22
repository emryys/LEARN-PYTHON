### DICTIONARIES ###
## its like almost real dictionaries there are keys and values. keys are identifiers and values are the data

student = {'name': 'Serden','age': 21, 'courses': ['Math','CompSci']}
print(student) #this prints out the all keys and values
print(student['name']) #if we exactly print our get the name key's value
print(student.get('name')) #same as above but if we try to get a key that is not in our dict it return 'none' by default 
print(student.get('not in list')) # not in list is a key that is not in our list :)))
print(student.get('not in list','there is a no key such this')) #by default we get none but we changed it to anything else
print(student['courses'])


# our dictionary can be just about anything for example the student dictionary is composed of
# a string an integer and a list also for this example all of the keys are strings but they can be any immutable data types
# for example since 1 is a immutable thing it can be used as a key
student2 = { 1: 'Serden','age': 21, 'courses': ['Math','CompSci']}
print(student2)

##lets look at how we can add a new entry to our dict
student['phone'] = 5232342 #it there is already a key named phone then it would be updated by new input
student['name'] = 'Serden Sait' #this will update 'Serden' to 'Serden Sait'
print(student)

# lets say our dict is very large in size and we wanna update many key value then we can use update method
student.update({'age':25,'name':'eranil','anything':'everything'}) #update method take a dict as an input and update the original dict instance
print(student)

#what if we wanna delete a specific key and its value
del student['anything'] #this will remove the anything key from the student dict
print(student) 

#another method is pop method as we remember from lists lecture
popped = student.pop('phone') #this will pop the phone key out
print(popped) 
print(student) #to see really it is removed from the dict

print(len(student)) #prints the how many keys(identifiers) in our dict
print(student.keys()) # as you guess it will print out only the keys
print(student.values()) #print outs only the values
print(student.items()) #print outs both keys and values

for key in student: #it only prints out keys
    print(key)

for key,value in student.items(): #it both prints out keys and values
    print(key,value)

#resource : https://www.youtube.com/watch?v=daefaLgNkw0&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=5



