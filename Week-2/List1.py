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

