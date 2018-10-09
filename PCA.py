# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:46:32 2018

@author: 
"""

import numpy as np
from scipy import linalg as LA

n1=-0.4
n2=-0.02
n3=0.31

matrix = np.array([[1,n1,n2],
                   [n1,1,n3],
                   [n2,n3,1]])
    
print(matrix)
e_vals, e_vecs = LA.eig(matrix)
print("eigenvalues: ",e_vals)
print("Eigenvalue 1 = ", max(e_vals.real))
print("Eigenvalue 2 = ", np.median(e_vals.real))
print("Eigenvalue 3 = ", min(e_vals.real))
print("Variance of total data:")
print("Eigenvalue 1 = ", max(e_vals.real)/3*100)
print("Eigenvalue 2 = ", np.median(e_vals.real)/3*100)
print("Eigenvalue 3 = ", min(e_vals.real)/3*100)
print("eigenvectors: ",e_vecs)

print("number 1:", e_vecs[0,0], e_vecs[1,0], e_vecs[2,0])
print("number 2:", e_vecs[0,1], e_vecs[1,1], e_vecs[2,1])
print("number 3:", e_vecs[0,2], e_vecs[1,2], e_vecs[2,2])
