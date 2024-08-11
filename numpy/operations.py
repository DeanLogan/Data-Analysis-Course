import numpy as np

arr = np.arange(4) # create an array from 0 to specified range (in this case 4)
print(arr)

print(arr+10) # creates a new array and returns the new array with 10 added onto it 

arr += 10 # this operation will modify arr
print(arr)

arr2 = np.array([1,2,3,4])

print(arr * arr2) # you can also perform operations with other arrays