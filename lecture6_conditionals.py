## IF STATEMENTS

if True:
    print('Conditional was True') #since the conditon is true this line works

if False:
    print('Conditional was True') #since the condition is false compiler cannot reach this line

language = 'Python'
#while typing statements make sure it is aligned with 'if' keyword
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
elif language == 'Javascript':
    print('Language is Javascript')
else:                          
    print('No match') 

# COMPARISIONS  #############
# EQUAL :            ==     #
# NOT EQUAL :        !=     #
# GREATER THAN :     >      #
# LESS THAN :        <      #
# GREATER OR EQUAL : >=     #
# LESS OR EQUAL :    <=     #
# OBJECT IDENTITY :  is     #
#############################

# what is the difference between 'is' and '==' with 'is' statement we're actually checking if values have
# the same ID or basically whether they are the same object in memory

# if you're coming from another programming language you may be wondering if python has a switch-case statement
# and if you don't know what a switch-case statement is it is a basically to check multiple values and python doesn't
# have a switch case and the reason is because if elif and else statements are pretty clean enough to do this already
# so if we wanted to check another statement we can just keep adding the elif statement 

## BOOLEAN OPERATIONS #and #or #not
user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in: #both 1st and 2sn statement should be true
    print('Admin Page')
else: #if neither of these statemts above is true
    print('Bad Creds')

user = 'Admin'
logged_in = True
if user == 'Admin' or logged_in: #either 1st or 2nd statement should be true
    print('Admin Page')
else: #if both of the statemts above is true
    print('Bad Creds')

# not operation is only used to change the state of a boolean it makes trues falses and falses trues

if not logged_in:
    print('Please log in')
else:
    print('welcome')

# two object can actually be equal and not be the same object in memory and
# 'is' statement checks whether they are the same object in memory

a = [1, 2, 3] #list
b = [1, 2, 3] #another list
print(a == b) #this returns true because the two lists are equal 
print(a is b) #this returns false because these are two different objects in memory 
# the 'is' comparision really checks the two variable have the same ID as it can bee seen a and b don't have same id
print(id(a))
print(id(b))

## BUT IF I SAY b = a. THEN a AND b WOULD HAVE THE SAME ID AND 'is' OPERATOR WOULD RETURN TRUE
## FOR EXAMPLE
c = a #(this is my opinion) when we use this kind of assignment python does not create a new variable with a new adress it only uses a simple pointer to point
print(a is c)
print(id(a) == id(c)) #they are the same in memory level

#NOW LOOK AT THE ALL FALSE VALUES THAT PYTHON EVALUATES

##### FALSE VALUES #####
# False
# None
# Zero of any numeric type
# Any empty sequence. For example, '',(),[]
# Any empty mapping. For example, {}        

condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = []

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = {} #empty dictionary not set

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


# SO WE CAN CONTROL IF A LIST, STRING, TUPLE OR DICT IS WHETERHER EMPTY OR NOT WITHOUT ANY NEED TO AN EXTRA METHOD

# resource : https://youtu.be/DZwmZ8Usvnk?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU




