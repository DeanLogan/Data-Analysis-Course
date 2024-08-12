import numpy as np
import sys

# Memory size of Python integers
print(sys.getsizeof(1))  # An integer in Python is > 24 bytes
print(sys.getsizeof(10**100))  # Long integers are even larger

# Memory size of NumPy integers
print(np.dtype(int).itemsize)  # Size of a NumPy integer (typically 4 or 8 bytes)
print(np.dtype(np.int8).itemsize)  # Size of a NumPy int8 (1 byte)

# Performance comparison
arr = np.arange(100000)  # Create an array with 100,000 elements
print(np.sum(arr ** 2))  # Sum of squares of the array elements

# Linear Algebra operations

# Matrix A (3x3)
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Matrix B (3x2)
B = np.array([
    [6, 5],
    [4, 3],
    [2, 1]
])

# Matrix multiplication
print(A.dot(B))  # Matrix multiplication using dot method
print(A @ B)  # Matrix multiplication using @ operator

# Transpose of matrix B
print(B.T)  # Transpose of matrix B

# Matrix multiplication with transpose
print(B.T @ A)  # Matrix multiplication of B transpose and A

# Additional Linear Algebra operations

# Identity matrix
I = np.eye(3)
print(I)  # 3x3 Identity matrix

# Determinant of a matrix
det_A = np.linalg.det(A)
print(det_A)  # Determinant of matrix A

# Inverse of a matrix (if it exists)
try:
    inv_A = np.linalg.inv(A)
    print(inv_A)  # Inverse of matrix A
except np.linalg.LinAlgError:
    print("Matrix A is singular and cannot be inverted.")

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)  # Eigenvalues of matrix A
print(eigenvectors)  # Eigenvectors of matrix A

# Solving a system of linear equations Ax = b
b = np.array([1, 2, 3])
try:
    x = np.linalg.solve(A, b)
    print(x)  # Solution to the system of equations
except np.linalg.LinAlgError:
    print("Matrix A is singular and the system cannot be solved.")