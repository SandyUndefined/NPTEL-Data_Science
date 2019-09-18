# Creating Sets
age = {20, 25, 23, 21, 25}  # No particular order
print(f'Creating Sets', age)  # No Duplicate values
name = {"sam", "sandy", "sharma", "sharmaJi"}
print(f'Creating Sets : ', name)


# Modifying Sets
# 1. using add()
name.add("sandeep")
print(f'Modifying using add() : ', name)
# 2. using discard() : removes matching element
name.discard("sam")
print(f'using discard() : ', name)


# Set Operations
Junior_datascientist = {"R", "Python", "tableau"}
datascientist = {"R", "Python","Java", "Scala", "tableau"}
print(Junior_datascientist, datascientist)
# 1. Union()
# Junior_datascientist.union(datascientist)
print(f'Union() : ', Junior_datascientist.union(datascientist))
# 2. Intersection()
# Junior_datascientist.intersection(datascientist)
print(f'Intersection : ', Junior_datascientist.intersection(datascientist))
# 3. Difference()
#  Junior_datascientist.difference(datascientist)
# A - B
print(f'Difference : ', Junior_datascientist.difference(datascientist))
# B - A
print(f'Difference : ', datascientist.difference(Junior_datascientist))
# 4. Symmetric difference
print(f'symmetric difference : ', Junior_datascientist.symmetric_difference(datascientist))