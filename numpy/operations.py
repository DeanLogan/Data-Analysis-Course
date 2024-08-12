import numpy as np

arr = np.arange(4)  # Create an array with values from 0 to 3
print(arr)  # Output: [0 1 2 3]

print(arr + 10)  # Creates a new array by adding 10 to each element of 'arr', Output: [10 11 12 13]

arr += 10  # In-place addition, modifies 'arr' by adding 10 to each element
print(arr)  # Output: [10 11 12 13]

arr2 = np.array([1, 2, 3, 4])  # Create a new array 'arr2' with specified values
print(arr2)  # Output: [1 2 3 4]

print(arr * arr2)  # Element-wise multiplication of 'arr' and 'arr2', Output: [10 22 36 52]