# integer is a whole number
# float is a decimal number

num = 3 #integer
print(type(num))  #gives the type of the variable

############################################################################################
# ARITHMETIC OPERATORS :      #      COMPARTISIONS : Boolen values either false or true
# ADDITION :      3 + 2       #      Equal:            3 == 2
# SUBSTRACTION:   3 - 2       #      Not Equal:        3 != 2
# MULTIPLICATION: 3 * 2       #      Greater than:     3 > 2
# DIVISION:       3 / 2       #      Lower than:       3 < 2
# FLOOR DIVISION: 3 // 2      #      Greater or equal: 3 >= 2
# EXPONENT:       3 ** 2      #      Less or equal:    3 <=2
# MODULUS :       3 % 2       #
############################################################################################

print(3/2) # 1.5 in python3 but 1 in phyton2
print(3//2) # 1 its rounded to smallest nearest integer
print(3**2) # 9

num += 1  #incrementing and it can be used other operators too

# there are some built in functions in python

print(abs(-3))
print(round(3.75))
print(round(3.75,1)) # it says how many digits it must round
print(round(3.1))
print(round(3.5))

num1 = 3
num2 = 2
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)
print(num1 == num2)
print(num1 != num2)

#if we don't know the type of a variable, this can occur
num3 = '100'
num4 = '200'
print(num3 + num4)

# in this case we should correct it with casting 
num3 = int('100') ## or num3 = int(num3)
num4 = int('200') ## or num4 = int(num4)
print(num3 + num4)

# Resource : https://www.youtube.com/watch?v=khKv-8q7YmY&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=3