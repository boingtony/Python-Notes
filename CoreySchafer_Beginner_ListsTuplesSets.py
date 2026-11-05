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

# prints new list of courses including Art and Biology items
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

# creates a new variable with indexes in list
nums = [1, 5, 2, 4, 3]

print(nums)

# sorts indexes in list from lower value to higher
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

# prints only the mininum and maximum index inside of list
print(min(nums))
print(max(nums))

# prints the sum of the indexes inside of list
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

# creates a for loop to show index of what item we are on in courses list
# prints the index of the item we are on and the items in courses list
for index in enumerate(courses):
    print(index, courses)
