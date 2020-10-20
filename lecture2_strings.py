message = 'Hello World'

# if my message would be 'Bob's World' then the single quote will cause an error
# in order to eleminate this error  double quote can be used as in the example

message2 = "Hello World"

print('Hello World') 

multiple_lines = """this 
variable can hold
string of more then one line"""

#   OR #

print(message)
print(message2)
print(multiple_lines)

# len(message) : gives the lenght of the string
print(len(message2))

# we can access the indexes of the string
print(message[0]) # prints 'H' which is the first character
print(message[10]) # prints 'd' which is the last character
print(message[0:5]) # prints the first element of the string to fifth element(not included)
print(message[:5]) # same as above prints 0 to 5th index(not included)
print(message[6:]) #prints 6th index to last index(included)

# there are some methods which operates on objects . message variable belongs to an object and therefore
print(message.lower()) #turn all string to lowercase letters
print(message.upper())   #turn all string to uppercase letters
print(message.count('Hello')) #the count method counts the number of the parameter inside the string
print(message.count('l')) #counts the number of 'l's inside the string which is 3
print(message.find('World')) #find method on the other hand finds the index that our message is at which is 6 in this case

#replace method basically finds the string it is given in first parameter and replace it with the second parameter
changed_message = message.replace('World','Universe')
print(changed_message) 

## CONCATENATING ##
greeting = 'Hello'
name = 'Serden'
new_message = greeting + ', ' + name
print(new_message)

## PLACE HOLDERS ##
# the new_message above is seeming a little bit awkward becase plus signs, commas etc. There is a better way to do this
message_placeholders = '{}, {}. Welcome!'.format(greeting.upper(),name) #by using the format method on the string we can assing strings to our placeholders.
print(message_placeholders)

## for python 3.6 or higher python users there is fstrings
message = f'{greeting}, {name}. Welcome!' #this method is a more compact than the above because methods can be applied in placeholders also.
message_upper = f'{greeting.lower()}, {name.upper()}. Welcome!'
print(message_upper)

# There are a lot of methods and we can see what methods we have on our variable by typing this
print(dir(name)) 
# WE CAN ALSO SEE THE DETALID INFO OF METHODS ON STRINGS BY
print(help(str))
# AND FOR DETALIED INFORMATION OF ONLY ONE METHOD
print(help(str.lower)) 

# RESOURCE https://www.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2
