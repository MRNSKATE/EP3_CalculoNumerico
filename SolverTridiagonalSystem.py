#Marco Antônio Rudas Napoli, n° USP: 11857970

from cmath import cos, pi
import numpy as np

def vector_discovery_U_L(a,b,c,n):
    U = np.zeros(n)
    L = np.zeros(n)
    for i in range(n):
        if i ==0:
            U[i] = b[i]
        else: 
                L[i] = a[i]/U[i-1]
                U[i] = b[i] - L[i]*c[i-1]
    return L,U 

def solution_system(l,u,c,d,n):    
    Y = np.zeros(n)
    X = np.zeros(n)
    for i in range(n):
        if i ==0:
            Y[i] = d[i]
        else:
            Y[i] = d[i] - (l[i]*Y[i-1])
    X[n-1] = Y[n-1]/u[n-1]
    for i in range(n-2,-1,-1):
            X[i] = (Y[i] - (c[i]*X[i+1]))/u[i]
    return X
    
def initial_solution(a, b, c, d, n):
    l, u = vector_discovery_U_L(a,b,c,n)
    X = solution_system(l,u,c,d,n)
    print("Matriz X resultante:\n", X)
