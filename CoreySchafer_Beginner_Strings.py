# set welcome_message variable
welcome_message = 'Hello World'

# example of double quoted string
# use double quotes for strings with single quotes in the text
example_message = "Robert's dog is fast"

# example of string with multiple lines
# use three double quotes for multi-lined strings
example_message_lined = """Robert's dog is fast.
You have to see it."""

# print welcome message
print(welcome_message)

# print example message
print(example_message)

# print example message lined
print(example_message_lined)

# print the numerical length of the string
print(len(welcome_message))

# print the specified character in the string. this is an index
# 0 being the first character, this prints H
print(welcome_message[0])

# print a range of specified characters. called slicing
# 0 through 5 being Hello. the first index is inclusive, but the last is not
# [:5] will achieve the same effect, as it starts from the beginning
print(welcome_message[0:5])

# prints characters 6 through 11, being World
# [6:11] has same effect as it continues until the end of the string
print(welcome_message[6:])

# uses .lower() method to make the called string lowercase only
print(welcome_message.lower())

# uses .upper() method to make the called string uppercase only
print(welcome_message.upper())

# uses .count() method to count number of specified characters in the string
# returns 1, as there is 1 instance of Hello in the string
print(welcome_message.count('Hello'))

# uses .find() method to find index of specified characters in the string
print(welcome_message.find('World'))

# example of .find() method looking for characters not in the string
# returns value of -1 as there is no value for specified characters
print(welcome_message.find('NotHere'))

# variable to show .replace() method
replace_message = 'Hello World'

#creates a new variable that uses the .replace() method to change World to Guys
new_replace_message = replace_message.replace('World', 'Guys')

# prints string using above .replace()
print(new_replace_message)

# uses .replace() to set variable to replaced string
replace_message = replace_message.replace('World', 'Guys')

# prints string with .replace() change to variable
print(replace_message)

# new variables for a greeting message
greeting = 'Hello'
name = 'Robert'

# concatenates above variables into a greeting message
# this leaves no space between Hello and Robert strings
greeting_message = greeting + name

# prints greeting message
print(greeting_message)

# adds a string between variables for correct presentation
new_greeting_message = greeting + ', ' + name

# prints new fixed greeting message
print(new_greeting_message)

# its hard to keep track of all concatenations between lots of strings
# .format() helps as you can write the string and place variables within it
formatted_greeting_message = '{}, {}. Welcome!'.format(greeting, name)

# prints formatted greeted message that uses .format()
print(formatted_greeting_message)

# uses fstring .format() to write the variables in the placeholder brackets
# code reads more clearly than just using .format() method
fstring_greeting_message = f'{greeting}, {name}. Welcome!'

# prints greeting message using fstring format
print(fstring_greeting_message)

# fstring example with code inside the placeholder brackets
# makes the variables use the .upper() method
fstring_greeting_message_upper = f'{greeting.upper()}, {name.upper()}. Welcome!'

# prints fstring greeting message now capitalized
print(fstring_greeting_message_upper)

# shows all available methods that can be used with variable
# print(dir(name))

# shows documentation on how to work with string variable
# help(str))

# shows documentation on method used with variable
# help(str.lower))