import numpy as np

# Array creation methods
arr = np.array([1, 2, 3, 4]) 
print(arr)  # np array example

arr = np.zeros((2, 3))  # creates an array of zeros with shape (2, 3)
print(arr)

arr = np.ones((3, 2))  # creates an array of ones with shape (3, 2)
print(arr)

arr = np.arange(10)  # creates an array with values from 0 to 9
print(arr)

arr = np.linspace(0, 1, 5)  # creates an array with 5 values evenly spaced between 0 and 1
print(arr)

# Multi-indexing example
arr = np.array([1, 2, 3, 4])
print(arr[[0, 2, -1]])  # multi-indexing example

# Setting type of array
arr = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(arr.dtype)

# Dimensions and shapes
arr = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(arr.shape)  # gives the shape (the number of rows followed by the number of columns)
print(arr.ndim)  # gives the number of dimensions (sum of the number of rows and columns)
print(arr.size)  # gives the total size, the total count of elements within the array

# If the arrays dimensions do not match it will turn into an object instead.

# Slicing of matrices
print(arr[:, :2])  # this will select every row and then within each row everything from the first column to the 2nd. (arr[d1, d2, d3, etc])

# Reshaping arrays
arr = np.arange(6).reshape((2, 3))  # reshapes the array to shape (2, 3)
print(arr)

# Array arithmetic
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # element-wise addition
print(arr1 * arr2)  # element-wise multiplication

# Broadcasting
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr + 10)  # adds 10 to each element of the array

# Boolean indexing
arr = np.array([1, 2, 3, 4, 5])
print(arr[arr > 3])  # selects elements greater than 3

# Below are some statistical operations that numpy offers for arrays
print(arr.sum())  # sum of all elements
print(arr.mean())  # mean of all elements
print(arr.std())  # standard deviation of all elements
print(arr.var())  # variance of elements within the array (can also calculate for the specific axis)