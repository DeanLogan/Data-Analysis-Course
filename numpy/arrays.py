import numpy as np

arr = np.array([1,2,3,4]) 
print(arr) # np array eg

print(arr[[0, 2, -1]]) # multi-indexing example

arr = np.array([1,2,3,4,5], dtype=np.int8) # setting type of arr
print(arr.dtype)

# Dimensions and shapes
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(arr.shape) # gives the shape (the number of rows followed by the number of columns)

print(arr.ndim) # gives the number of dimensions (sum of the number of rows and columns)

print(arr.size) # gives the total size, the total count of elements within the array

# If the arrays dimensions do not match it will turn into an object instead.

# SLicing of matrices

print(arr[:, :2]) # this will select every row and then within each row everything from the first column to the 2nd. (arr[d1, d2, d3, etc])

# Below are some statical operations that numpy offers for arrays
print(arr.sum()) # sum of all elements
print(arr.mean()) # mean of all elements
print(arr.std()) # standard deviation of all elements
print(arr.var()) # variance of elements within the array (can also calculate for the specific axis)