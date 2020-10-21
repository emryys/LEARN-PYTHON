## LISTS ##

courses = ['History', 'math', 'physics', 'compsci'] 
print(courses)
print(len(courses)) #gives the number of elements in list
print(courses[0]) #gives the first item
print(courses[3]) #gives the last item since the lenght is 4
print(courses[-1]) #more convenient way to access to last item
print(courses[-2]) # it can be used to access elements from the end. it gives physics

## THESE ARE CALLED SLICING BECAUSE IT IS SLICED VERSION OF THE LIST
print(type(courses[0:2])) #it gives a sublist
print(courses[0:2]) # it gives the 0th 1th elements of the list
print(courses[:2]) # same as above no need to write 0
print(courses[2:]) #it gives the sublist starting from 3rd element to last element(included)
print(type(courses[0:2])) #it gives a sublist

courses.append('Art') #it adds an item to the end of the list
print(courses) 
courses.insert(0,'Art') # if we wanna insert an item to the list we can use insert function and specify the index we wanna insert
print(courses) 

courses2 = ['art', 'education']
#lets say we wanted to add courses2 to the beginning of courses and we can try this but unfortunately it won't work
courses.insert(0,courses2)
print(courses)  #as it is seen it adds the list courses2 to 0th index of courses which makes sense because the elements of list can hold any type of value

# so what is the solution : extend function
courses.extend(courses2) #it extends the list( adds items to the end) as expected
print(courses)

#what if we wanna try to remove an item
courses.remove('art')
print(courses)

#also there is a method called pop
popped = courses.pop() #by default it pops the last item and returns the value of the item that it popped. It is useful for stacks and queues
print(popped)
print(courses)

#lets look at the some sorting methods
#lets say we wanna reverse the list it is pretty easy in python
courses.reverse()
print(courses)

#lets define the courses again to see more easily
courses = ['math', 'physics' , 'art', 'education']
print(courses)
courses.sort() #it sorts the list in the alpabetical order
print(courses)

courses_nums = [1, 2, 4, 5, -1, 10]
print(courses_nums)
courses_nums.sort() #if we use the method sort for list of numbers it sorts the list in ascending order
print(courses_nums)

#if we wanna sort both courses and courses_nums then probably the first thing it comes our mind to first sort the lists and reverse them
# but there is a easier way to do this in one line
courses = ['math', 'physics' , 'art', 'education']
courses_nums = [1, 2, 4, 5, -1, 10]
print(courses)
print(courses_nums)
courses.sort(reverse=True) #sorts the list in descending alphabetical order
courses_nums.sort(reverse=True) #sorts the list in descending order
print(courses)
print(courses_nums)

#lets say we wanted to sort our list just for show we don't want our list to be altered. therefore we should use functions instead of methods
print(sorted(courses_nums)) #again it is in ascending order

#built-in function that we can use on lists
print(min(courses_nums)) #it gives the minimum number in the list
print(max(courses_nums)) #it gives the maximum number in the list
print(sum(courses_nums)) #it gives the sum of the numbers in the list

#if we want to find the index of a desired element
print(courses)
print(courses.index('art')) 
# print(courses.find('art')) this won't work because find method is attributed to string object

# if we check only whether it exists or not we can use 'in'
print(courses)
print('art' in courses)
print('Art' in courses) #it gives false becuase pyhton is case-sensitive

# what if we wanna get the each item separately then we can use for loop
# this item variable will be equal each item in the list one at a time and prints them
for item in courses: #we can name the 'item' variable anything we want. for example we can use 'name'
    print(item)     #why this line is indented. it describes this line is in for loop

# THIS ENUMARATE FUNCTION RETURNS TWO VALUES IT RETURNS THE INDEX WE ARE ON AND THE VALUE
# SO INSTEAD OF JUST GETTING THE COURSE HERE WE'RE ALSO GOING TO NEED TO GET THE INDEXES
for index, course in enumerate(courses, start=1): #if we want numeration not to start from 0 we can specify it like this but by default it starts from 0
    print(index, course)


# IF WE WANT TO CONVERT OUR LIST TO A STRING SEPARATED BY A SPECIFIED CHARACTER WE CAN USE JOIN METHOD
course_str = ', '.join(courses)
print(course_str)

# WE CAN ALSO CONVERT STRING TO LIST
new_list = course_str.split(', ') # it splits the string every time it sees a comma
print(new_list)


#### TUPLES ###

# tuples are very similar to list but with one major difference we can't modify tuples. in programming jargon lists are called mutable
# and tuples are called immutable

# lists example(mutable)
list_1 = ['history', 'math', 'physics', 'compsci']
list_2 = list_1

print(list_1)
print(list_2)

#in here we only changed the first element of the list_1 but since the lists are mutable the first element of
# list 2 is also changed 
list_1[0] = 'art'  

print(list_1)
print(list_2)

# tuple example (immutable)
tuple_1 = ('history', 'math', 'physics', 'compsci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#in here we only changed the first element of the list_1 but since the lists are mutable the first element of
# list 2 is also changed 
# tuple_1[0] = 'art'  we cant do this if we try to do this compiler will give an error



#### SETS
cs_courses = {'history', 'math', 'physics', 'compsci', 'math'}
print(cs_courses) #this will return the above values in random orders and it deletes the duplicates
# the main reason for that is sets are used generally to check if a item in a set or to delete the duplicates.
print('math' in cs_courses) #it gives true. it is valid for lists and tuples also but sets are optimized for this

art_courses = {'history', 'math', 'art', 'design'}
print(cs_courses.intersection(art_courses)) # it will gives the intersection of these two courses.
print(cs_courses.difference(art_courses)) # it will gives the differences of these two courses.
print(cs_courses.union(art_courses)) # it will gives the union of these two courses.

#last thing in this course is to create empty lists tuples and sets

# EMPTY LISTS
empty_list = []
empty_list = list()

# EMPTY TUPLES
empty_tuple = ()
empty_tuple = tuple()

# EMPTY SETS
#empty_set = {} this isn't right! it's a dict
empty_set = set()

print(empty_tuple,empty_list,empty_set)



