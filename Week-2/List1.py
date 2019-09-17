# Creating a List
id = [1, 2, 3, 4]
name = ["sam", "sandy", "sharma", "sharmaJi"]
n = 4
lists = [id, name, n]
print(f'Creating a List:', lists)

# Indexing
# 1.Positive
print(f'Positive Indexing:', id[2])  # start from left most
# 2.Negative
print(f'Negative Indexing:', name[-1])  # start from right most

# Accessing of a list
# 1.Top-level component
print(f'Accessing list from top level component :', lists[2])
# 2.Sub-level component
print(f'Accessing list from sub level component :', lists[0][0])


# Modifying a component of list
# Using Index Value
lists[2] = 5
print(f'Modifying  component of list Using Index Value (top-level): ', lists)
lists[1][0] = "Sandeep"
print(f'Modifying  component of list Using Index Value (Sub-level): ', lists)


# Using inbuilt function: it added element at last
# append()
# syntax = list_name[index].append(object)

# Adding a element to a list
lists[0].append(5)
print(f'Adding a element to a list : ', lists)
lists[1].append("undefined")
print(f'Adding a element to a list : ', lists)

# Adding a list to a List
age = [22, 23, 21, 30, 25]
lists.append(age)
print(f'Adding a list to a List: ', lists)


# Using insert(): it adds element to a specified position
lists[0].insert(0, 6)
print(lists)


# Removing elements from a lists
# 1. del : removes a element at a specified index number
del lists[3]
print(lists)
# 2. remove() : removes the first matching element from a list.....at first occurrence
lists[0].remove(6)
print(lists)
# 3. pop() : display the object that has been removed
lists[0].pop(4)
print(lists)

