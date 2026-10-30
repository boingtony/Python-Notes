# arithmetic operators:
# addition:         3 + 2
# subtraction:      3 - 2
# multiplication:   3 * 2
# division:         3 / 2
# floor division:   3 // 2
# exponent:         3 ** 2
# modulus:          3 % 2

# prints result of arithmetic operators for reference
# addition: adds 
print(3 + 2)
# subtraction: subtracts 
print(3 - 2)
# multiplication: multiplies 
print(3 * 2)
# division: divides
print(3 / 2)
# floor division: divides and rounds down to nearest whole number
print(3 // 2)
# exponent: works with powers
print(3 ** 2)
# modulus: gives remainder after division
print(3 % 2)

# comparisons:
# equal:            3 == 2
# not equal:        3 != 2
# greater than:     3 > 2
# less than:        3 < 2
# greater or equal: 3 >= 2
# less or equal:    3 <= 2

num_1 = 3
num_2 = 2

# prints result of comparison operators for reference
# will return as a True/False boolean
# equal:
print(num_1 == num_2)
# not equal:
print(num_1 != num_2)
# greater than:
print(num_1 > num_2)
# less than:
print(num_1 < num_2)
# greater or equal:
print(num_1 >= num_2)
# less or equal:
print(num_1 <= num_2)

# set variable to integer 
num = 3

# shows variable is class int/integer
print(type(num))

# set variable to float
float_num = 3.14

# shows variable is class float
print(type(float_num))

# calculations to show order of operations work in python
# follows BIDMAS rules
print(3 * 2 + 1)
print(3 * (2 + 1))

# shows how to increment values. works with other operators
increment_num = 1
increment_num += 1
print(increment_num)

# shows increment working with multiply operator
increment_mult_num = 1
increment_mult_num *= 10
print(increment_mult_num)

# shows absolute value when working with negative numbers
print(abs(-3))

# shows rounding values when working with floats
print(round(3.75))
# shows rounding values to a given argument
# note: when a number is exactly half way, python rounds to the nearest even number
# called 'banker's rounding'
# nearest even number is 4, so 3.5 rounds up to 4
print(round(3.5))
# the 1 says to round to the first digit after decimal
print(round(3.75, 1))

# variables that look like integers but are strings
string_num_1 = '100'
string_num_2 = '200'

# shows the variables are strings that are being concatenated together
print(string_num_1 + string_num_2)

# casts the strings from variable into integers in new variable
# note: int() only works if the number looks like a whole number
casted_string_num_1 = int(string_num_1)
casted_string_num_2 = int(string_num_2)

# adds and prints the integers from these variables
print(casted_string_num_1 + casted_string_num_2)
