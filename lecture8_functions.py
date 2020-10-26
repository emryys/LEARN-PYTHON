## FUNCTIONSS ##
# functions are basically some instructions packed together to perform a specific task
# functions also allow use to use the code without repeating ourselves
# to create a function we'll use the 'def' keyword

#also instead of changing everthing in everyplace we can just change the function that affects everywhere
# this is called keeping the code 'DRY' namely don't repeat yourself

def hello_func(): #we add our paramters in those parantheses
    pass #this pass keyword pass this function. we define function but not define the instructions yet

#to execute the function
hello_func() #we need these parantheses to execute the func if we don't put them, it will be equal the memory adress
print(hello_func) #<function hello_func at 0x00000212DE359310>
print(type(hello_func)) #<class 'function'> ; it returns a class adress

def hello_function():
    print('Hello Function!')

hello_function() #we executed the function with empty parameters

def hello_function2():
    return 'Hello Function2!'

hello_function2() #it doesn't give us the 'Hello Function!' output because this statment is only equals that string
# and it cannot be shwon in the output unless we print it out.
#but we can print it our like this
print(hello_function2()) #it gives the expected result

#when we call our function its just the type of value that is returned from the function. Namely,
# we can use the methods directly on the function because it is the same.

print('Hello Function2'.upper())
print(hello_function2().upper()) #both are the same thing.

#now lets add some parameters to our function

def hello_func3(greeting):
    return f'{greeting}, Function' #here we used fstrings (f'aa')
def hello_func4(greeting):
    return '{}, Function'.format(greeting) #here we used the string with format method
#BOTH OF THE FUNCTIONS ABOVE ARE THE SAME

print(hello_func3('selamun aleykum')) #since these functions expect a greeting parameter we must add it when we call it
print(hello_func4('selamun aleykum')) 

# the greeting variable does not affect any variable outside of the function it is a local variable what is only defined in the function 
# and when the function is done it is deleted from the ram

def hello_func5(greeting, name = 'You'): #now we have 2 parameters and when the function is called and no parameter added about name it is 'You' by default
    return f'{greeting}, {name}'

print(hello_func5('hello')) #as you see no value is added for the name parameter and it printed hello, You
print(hello_func5('Hello','Serden')) 
#         OR                 #
print(hello_func5('HELLO',name = 'Serden')) # you can use this execution statement 


## a little bit advanced ##

def student_info(*args, **kwargs): ## ALLOWS US TO ACCEPT AN ARBITRARY NUMBER OF POSITIONAL OR KEYWORD ARGUMENTS
    print(args)
    print(kwargs)   

# LET'S SAY THIS student_info() FUNCTION TAKES POSITIONAL ARGUMENTS THAT REPORESENT THE COURSES THAT THE STUDENT IS TAKING
# PLUS THE KEYWORD ARGUMENTS PASSED IN WILL BE RANDOM INFORMATION ABOUT THE STUDENTS SO AS YOU CAN SEE WE DON'T KNOW HOW MANY OF THESE
# POSITIONAL OR KEYWORD ARGUMENTS THAT WILL BE AND THAT'S WHY WE *args and **kwargs AND THE NAMES DON'T HAVE TO BE THESE args and kwargs

student_info('Math','Art',name = 'Serden')
student_info('Math','Art',name = 'Serden', age = 21 )

# args is actually a tuple(immutable) with all of our positional arguments  
# kwargs is actually a dictionary with all of our keyword values

##################################################################################################################

## now sometimes you might see a function call with arguments using the star or double star. now when it's used in that context
## it will actually unpack a sequence or dictionary and pass those values into the function individually 

courses = ['Math', 'Art']
info = {'name' : 'Serden', 'age' : 21 }
student_info(courses,info)
## output ## :
# (['Math', 'Art'], {'name': 'Serden', 'age': 21})
#  {}
# instaed of passing the values in individually and instead pass in the complete list and the complete dictionary
# as positional arguments
# if we use it like this
student_info( *courses, **info ) 
## output ##
# ('Math', 'Art') //// tuples of our unpacked positional arguments
# {'name': 'Serden', 'age': 21} //// dictionary of our unpacked keywords


## NOW TO UNIFY ALL THING WE LEARNED TRY TO WRITE A PROGRAM

# Number of days per month. First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """ Return TRUE for leap years, FALSE for non-leap years. """ ## This 3 double quote is called docstring and explains what the function does
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year,month):
    """Return number of days in that month in that year"""

    if not 1 <= month <= 12 :
        return 'Invalid Month'
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2017))
print(is_leap(2020))
print(days_in_month(2017,2))


# resource : https://youtu.be/9Os0o3wzS_I?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

 