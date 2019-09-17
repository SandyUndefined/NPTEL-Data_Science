# Creating a Tuple
id = (1, 2, 3, 4)
name = ("sam", "sandy", "sharma", "sharmaJi")
age = (22, 23, 25, 20)
salary = (2500, 2500, 2500, 2500)
tuples = (id,name,age,salary)
print(f'Creating a tuples', tuples)

# Indexing is same as list

# Accessing element
# Top level
print(f'accessing elements  top level: ', tuples[1])
# Sub level
print(f'accessing elements  sub level: ', tuples[1][2])

# Slicing
print(f'Slicing of a tuple: ', tuples[0:3])

# Built in functions
# length of tuple
print(f'Length of a tuple: ', len(tuples))
# Minimum
marks = (32, 12, 15, 17, 21)
print(f'prints minimum from a tuple: ', min(marks))
# Maximum
print(f'prints minimum from a tuple: ', max(marks))


# Combing two tuple
print(f'Concatenate tuple: ', tuples + marks)