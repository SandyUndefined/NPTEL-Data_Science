import numpy as np

# Creating matrix
a = np.matrix("1, 2, 3 ; 4, 5, 6; 7, 8, 9")


# Determinant of a matrix
det = np.linalg.det(a)
print(f'Determinant of a matrix : ', det)


# Rank of a Matrix
rank = np.linalg.matrix_rank(a)
print(f'Rank of a Matrix : ', rank)


# Inverse of a matrix
inverse = np.linalg.inv(a)
print(f'Inverse of a matrix : ', inverse)
# b = np.matrix("2, 1, 2;1, 0, 1;3, 1, 3")
# det = np.linalg.det(b)
# inverse = np.linalg.inv(b)
# print(inverse)  # Throws an array because det = 0


# System of Linear equation
# 3x+y+2z = 2
# 3x+2y+5x = -1
# 6x+7y+8z = 3
ab = np.matrix("3,1,2;3,2,5;6,7,8")
ba = np.matrix("2,-1,3").transpose()
solve = np.linalg.solve(ab, ba)
print(f'Solving System of Linear equation : ', solve)


# Application of System of Linear equation in Python
# 0.24 T1 + 0.15B1 + 0.18T2 + 0.07B2 = 75
# 0.65 T1 + 0.10B1 + 0.24T2 + 0.04B2 = 125
# 0.10 T1 + 0.54B1 + 0.42T2 + 0.54B2 = 200
# 0.01 T1 + 0.21B1 + 0.18T2 + 0.35B2 = 100

a = np.matrix("0.24,0.15,0.18,0.07;0.65,0.10,0.24,0.04;0.10,0.54,0.42,0.54;0.01,0.21,0.18,0.35")
b = np.matrix("75,125,200,100").transpose()
solution = np.linalg.solve(a, b)
print(f'Solution System of Linear equation : ', solution)
