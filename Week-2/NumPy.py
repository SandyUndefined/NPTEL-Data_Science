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