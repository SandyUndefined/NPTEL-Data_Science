import numpy as num
# Creating array using numPy
array = num.array([1, 2, 3, 4, 5])
print(f'Creating array using numPy : ', array)


# Generating array using built-in function

# 1. using linspace()

ab = num.linspace(start=1, stop=5, num=5,dtype=int, endpoint=True, retstep=False)  # dtype default is float
print(f'using linspace() : ', ab)

# 2. using arange()
ab = num.arange(start=1,stop=6,step=1)
print(f'using arange() : ', ab)

# 3. using ones()
ab = num.ones(5,int)
print(f'using ones() : ', ab)

# 4. using zeros()
ab = num.zeros(5,int)
print(f'using zeros() : ', ab)

# 5. Random values using in built function Random.rand()
ab = num.random.rand(5,2)
print(f'Random values using in built function Random.rand()  : ', ab)

# 6. Using logspce()
ab = num.logspace(start=1, stop=5, num=5, dtype=int,endpoint=True,)
print(f'Using logspce() : ', ab)


# Reshape an array
ab = num.arange(start=1,stop=10).reshape(3,3)
print(f'Reshape an array : ', ab)


# Array dimensions
ab = num.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f'Array dimensions : ', ab.shape)


# NumPy Operation

# 1. Addition
ba = num.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = num.add(ab, ba)
print(f'Array addition using numpy : ', result)

# 2. Multiplication
result = num.multiply(ab, ba)
print(f'Array multiplication using numpy : ', result)

# 3. other operations such as
# numpy.subtract()
# numpy.divide()
# numpy.remainder()


# Accessing elements of an array
print(f'accessing elements of an array using index number: ', ab[1, 0])

# Accessing whole row
print(f'accessing row of an array : ', ab[0:2])
# Accessing column
print(f'accessing column of an array : ', ab[:, 0])
# Accessing row
print(f'Accessing row : ', ab[0, :])


# Subset array
sub_array = ab[:2, :2]
print(f'Subset array : ', sub_array)
sub_array[0, 1] = 22
print(f'Modified values of subset array : ', sub_array)
print(f'after Modifying values of subset array the original array : ', ab)

# Modifying array using transpose()
transpose = num.transpose(ab)
print(f'Modifying array using transpose', transpose)

# Adding array using append() along the row wise
append = num.append(ab, [[11, 12, 13]], axis=0)
print(f'adding array using append() : ', append)

# Adding array using append() along the column wise
reshape = num.array([11, 12, 13]).reshape(3,1)
append = num.append(ab, reshape, axis=1)
print(f'adding array using append() : ', append)

# Adding array using insert()
insert = num.insert(ab, 1, [13, 14, 15], axis=0)
print(f'Adding array using insert() : ', insert)

# Deletion of an array
deleted = num.delete(ab, [13, 14, 15], axis=0)
print(f'Deletion of an array : ', deleted)