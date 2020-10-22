### LOOPS

nums = [1, 2, 3, 4 ,5]

# we're looping throug each value of our list and each time through the loop this num
# variable will be equal to the next item in the list 
for num in nums:
    print(num)

#break and continue keywords
#break keyword will compeletly break out of a loop 
#continue keyword will move on to the next iteration 
for num in nums:
    if num == 3:
        print('we found it')
        break #it compelety breaks the loop
    print(num)

for num in nums:
    if num == 3:
        print('we found it')
        continue #it goes next iteration and ignores the line after this line
    print(num)

for num in nums:
    for letter in 'abc':
        print(num,letter)

# there will be times when we just want to go thorugh a loop a certain number of times
# and there is a built-in function called range that is really useful for this 
# so lets say we wanted to just run through a loop ten times

for num in range(10): #by default it starts from 0
    print(num)

#by this way we can define our starting point
for num in range(1,12): #12 is not included
    print(num)

x = 0
while x < 10: #while this condition is true it keeps iterating until the condition is not met
    print(x)
    x += 1

#we can create infinite loops and when our condition is met we can break it
the_desired_condition = 1

while True:
    # definitions
    if the_desired_condition is True:
        break

