import numpy as np
import sympy as sp
from sympy import *

dim = int(input("Enter the dimension of the square matrix :"))

mat = []

for i in range(dim):
    temp_mat = []
    for j in range(dim):
        a = int(input(f"A{i}{j} :"))
        temp_mat.append(a)
    mat.append(temp_mat)
        
print("Entered matrix :")
print(np.matrix(mat))

x = symbols('x')
A = sp.Matrix(mat)
I = np.identity(dim, dtype=int)

eig =  solve(det(A-I*x),x)

print("Eigen values : ",eig)

    
sym = []
for i in range(dim):
    s = []
    for j in range(dim):
        if j==0:
            s.append(symbols(f'x{i}'))
    sym.append(s)        
            
sym = np.array(sym)

eig_vec = []

for i in eig:    
    print(f"Eigen vector for corresponding eigen value {i} : ")
    print(np.matrix(solve((A-i*I)*sym)))
    eig_vec.append(np.matrix(solve((A-i*I)*sym)))
    





