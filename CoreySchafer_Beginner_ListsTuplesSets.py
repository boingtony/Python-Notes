# creates a list variable with school course items
courses = ["History", "Math", "Physics", "Compsci"]

# prints list variable
print(courses)

# prints length of list in variable
print(len(courses))

# prints the first item in the list variable
print(courses[0])

# prints the last item in the list, as lists can use negative indexes
print(courses[-1])

# prints all items beginning from 0 up to, but not including, the second index
print(courses[:2])

# prints items from 2 all the way to the end. known as slicing
print(courses[2:])

# adds Physics item to the list in variable courses
courses.append("Physics")

# adds Biology item to the list at the beginning due to 0 index
courses.insert(0, "Biology")

# prints new list of courses including Physics and Biology items
print(courses)

# new variable with Art and Education
courses_2 = ["Art", "Education"]

# .insert() places those two items into courses 1 variable
# notably in their own brackets and both called by index 0
courses.insert(0, courses_2)

print(courses)

# .extend() places Art and Education in the list and able to be indexed the same
courses.extend(courses_2)

print(courses)

# removes the given entry from the list; in this case Math
courses.remove("Math")

print(courses)

# runs .pop() once, removing the last item, and stores the return in variable
popped = courses.pop()

# prints list without Education as it has been 'popped'
print(courses)

# prints the value removed by .pop()
print(popped)

# reverses order of the list
courses.reverse()

print(courses)

# removes nested list as .sort() below won't know if a list is less than a string
courses.remove(["Art", "Education"])

# arranges items in list by default alphabetically
courses.sort()

print(courses)

# creates a new variable with values in list
nums = [1, 5, 2, 4, 3]

print(nums)

# sorts values in list from lower value to higher
nums.sort()

print(nums)

# .sort() method but reversing their default order
courses.sort(reverse=True)
nums.sort(reverse=True)

print(courses)
print(nums)

# sorted function returns a sorted version of list
# then making new sorted_x variable from the returned list
# notably this leaves the original list unaltered
sorted_courses = sorted(courses)
sorted_nums = sorted(nums)

print(sorted_courses)
print(sorted_nums)

# prints only the minimum and maximum value inside of list
print(min(nums))
print(max(nums))

# prints the sum of the values inside of list
print(sum(nums))

# prints the index of CompSci within the list
print(courses.index("Compsci"))

# prints True or False depending on if the item is inside of the list
print("Art" in courses)
print("PhysicalEducation" in courses)

# creates a for loop. loops code inside of indentation to print item in list
# loops through the list putting each item (value) into item (variable) until all items are printed
# note: python takes the values out of variable one by one and assigns each to item (variable)
# item does not hold all values at once, hence it repeats after each item (value) in list
for item in courses:
    print(item)

# for loop using enumerate(), which gives back the index and the item together
# unpacks them into two variables: 'index' (position) and 'course' (value)
# prints the position number and the course on each loop
for index, course in enumerate(courses):
    print(index, course)

# the same as above, however start= dictates the starting point
for index, course in enumerate(courses, start=1):
    print(index, course)

# creates a new variable 'courses_str' which returns with .join() method on our list
# this returns the list as a string separated by hyphens, as dictated by " - "
courses_str = " - ".join(courses)

print(courses_str)

# takes our new string version of courses and turns it back into a list in a new variable
# list entries are dictated by the " - " so each instance of " - " is a new item
new_list = courses_str.split(" - ")

print(new_list)

# tuples vs lists example

# list - mutable. dictated by square brackets []
list_example = ["Happy", "Sad", "Angry", "Confused"]
list_example_2 = list_example

print(list_example)
print(list_example_2)

# replaced item 3 'Confused' with 'Tired'
list_example[3] = "Tired"

# shows both variables being changed. this is because the list that these variables are referencing has been changed
# this is because lists are 'mutable' meaning edits to the list will affect the variables using it
print(list_example)
print(list_example_2)

# tuple - immutable. dictated by round brackets ()
tuple_example = ("Happy", "Sad", "Angry", "Confused")
tuple_example_2 = tuple_example

print(tuple_example)
print(tuple_example_2)

# below comment will not work. as tuples are immutable, modifications to the tuple will not work
# tuple_example[3] = "Tired"

print(tuple_example)
print(tuple_example_2)

# sets

# sets. dictated by curly brackets {}
# sets dont care about order. their main use is to test whether a value is part of a set
# or to remove duplicate values. for example, adding "Math" to the list twice would remove the second in print
# sets will print in no particular order
sets_example = {"History", "Math", "Physics", "Compsci"}

print(sets_example)

# looks for item "Compsci" in sets_example variable. if found, prints True
# sets are optimized for below methods. moreso than lists or tuples
print("Compsci" in sets_example)

sets_example_compare = {"History", "Math", "PE", "RE", "IT"}

# prints the items that both variables share
print(sets_example.intersection(sets_example_compare))

# prints the items that sets_example has but sets_example_compare doesnt
print(sets_example.difference(sets_example_compare))

# prints items from both variables into one set
# any duplicate items only appear once
print(sets_example.union(sets_example_compare))

# empty lists, tuples, and sets

# empty_list = []
# empty_list = list()

# empty_tuple = ()
# empty_tuple = tuple()

# empty_set = {} does not work! this creates an empty dictionary
# empty_set = set()
