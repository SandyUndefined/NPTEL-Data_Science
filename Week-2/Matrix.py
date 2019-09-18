import numpy as np

# Creating matrix
ab = np.matrix("1, 2, 3, 4 ; 5, 6, 7, 8 ; 9, 10, 11, 12")
ba = np.matrix("11, 22, 33, 44 ; 55, 66, 77, 88 ; 99, 110, 111, 112")
print(f'Creating matrix : ', ab)
print(f'Creating matrix : ', ba)


# Modifying matrix
# 1. Insert()
insert = np.insert(ab, 1, (13, 14, 15), axis=1)  # axis =0 means row and axis = 1 column
print(f'Modifying matrix using insert : ', insert)

# 2. using index number
ab [0, 1] = 31
print(f'Modifying matrix using index number : ', ab)


# Accessing elements of a matrix
print(f'Accessing elements of a matrix : ', ab[1, :])
print(f'Accessing elements of a matrix : ', ab[:, 2])


# Matrix Operation
# 1. Addition
add = np.add(ab, ba)
print(f'Addition : ', add)
# 2. Subtraction
# Same as addition
# 3. Multiplication
ab = np.transpose(ab)
multiply = np.dot(ab, ba)
print(f'Multiplication : ', multiply)  # Whole matrix multiplication
ab = np.transpose(ab)
multiply = np.multiply(ab,ba)
print(f'Multiplication : ', multiply)  # Element wise matrix multiplication
