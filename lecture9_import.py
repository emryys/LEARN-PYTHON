import lecture9_imports_stdlibs as fi #when i run this it basically runs the lecture9 file in the same directory
from lecture9_imports_stdlibs import find_index,test #this allow us to import only the function and the test variable
from lecture9_imports_stdlibs import * #this line imports everything from the file

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi.find_index(courses,'Math') #we imported our modules as fi and we can use the method from it like this
print(index)
print(test)


#the difference between import * and directly importing is that we can't tell what comes from where
#not knowing the what comes form where can cause problems when we wanna track down the functions

#how does import knows where to look to import the module
# import command have specified paths to look for and we can see this paths by 
import sys
print(sys.path)
# as we can see from the output our working directory also in the paths if we want a module imported that is not our
# specified paths den we can add our path to sys.path list.
# as you can see sys.path is a list of paths and we know how to add and remove paths
sys.path.append('C:/Users/"Serden Sait"/Desktop')
print(sys.path) #as you can see we add a path manually

### random library from standart libraries
import random
random_course = random.choice(courses) #randomly selects a string from the list of courses
print(random_course)
### math library from standart libraries
import math
rads = math.radians(90)
print(math.sin(rads))
### datetime library from standart libraries
import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))
### os library from standart libraries
import os
print(os.getcwd()) #cwd:current working directory# gives the cwd
print(os.__file__) #says where does this py file locate


#resource : https://youtu.be/CqvZ3vGoGs0?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU