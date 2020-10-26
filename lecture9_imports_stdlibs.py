## learn how to import modules
## we'll start by importing modules that we've written and then we'll explore a bit of the standart library
## please see other lecture9 file in the same directory

print('Imported mymodule...')
test = 'Test String'

def find_index(to_search, target):
     '''Find the index of a value in a sequence'''
     for i,value in enumerate(to_search):
         if value == target:
             return i
     return -1

## when i imported this file this file will be 
#resource : https://youtu.be/CqvZ3vGoGs0?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU