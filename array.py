# Write code for array challenges below

import numpy as np

# Question 1
a = np.array([1,2,3,4])

def show_elements(arr):
    for el in arr:
        print(el)

show_elements(a)

# End of Question 1 Solution

# Question 2 - there are several ways to accomplist this

b = np.array([1,5,-2,10])

# iterative approach
def array_sum(numberArr):
    arrSum = 0
    for i in numberArr:
        arrSum = arrSum + i
    return arrSum

print(array_sum(b))

# recursive approach
def array_sum_recursive(numberArr):
    if len(numberArr) == 1:
        return numberArr[0]
    
    # Recursive case
    return numberArr[0] + array_sum(numberArr[1:])

print(array_sum_recursive(b))


# using NumPy sum operator
print(b.sum())

# End of Question 2 Solution