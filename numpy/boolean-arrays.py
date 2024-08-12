import numpy as np

arr = np.arange(5)

print(arr <= 3)  # returns true or false based on the condition
print(arr[arr >= 2])  # filters the arr
print(arr[arr > arr.mean()])  # filters the arr based on the mean of the arr
print(arr[~(arr > arr.mean())])  # Prints elements of the array 'arr' that are less than or equal to the mean of the array

# Combining multiple conditions
print((arr > 1) & (arr < 3))  # returns true or false based on both conditions
print(arr[(arr > 1) & (arr < 3)])  # filters the arr based on both conditions

# Using np.where
indices = np.where(arr >= 2)  # returns indices where the condition is true
print(indices)
print(arr[indices])  # filters the arr using the indices

# Boolean indexing with multiple conditions
print(arr[(arr < 1) | (arr > 2)])  # filters the arr where elements are less than 1 or greater than 2