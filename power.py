import numpy as np

#power method
def normalize(x):
    max = abs(x).max()
    newX = x / x.max()
    return max, newX

matrix = np.array([[2, 1], [0, -4]])

order = len(matrix)
x = np.ones((order, 1), dtype = int)

for i in range(10):
    x = np.dot(matrix, x)
    e, x = normalize(x)

print("Dominant Eigenvalue:", e)
print("Corresponding Eigenvector:\n", x)

#inverse power method
matrix = np.array([[10, -8, -4], [-8, 13, 4], [-4, 5, 4]])
matrix = np.linalg.inv(matrix)

order = len(matrix)
x = np.ones((order, 1), dtype = int)

for i in range(10):
    x = np.dot(matrix, x)
    e, x = normalize(x)

print("Smallest Eigenvalue:", 1 / e)