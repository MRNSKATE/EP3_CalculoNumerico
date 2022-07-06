from math import *
from cmath import cos, pi
import numpy as np

from SolverIntegralByString import *
from SolverTridiagonalSystem import *

def internal_multiplication(equal, xi_pre, xi, xi_pos, k_function, q_function, h):
    if equal == False:
        x_inf = 0
        x_sup = 1
        if xi > 0:
            x_inf = xi
        if xi_pos < 1:
            x_sup = xi_pos
        
        integer_function = "(-1/("+ str(h**2) + "))*((" + k_function + ")+(" + q_function + ")*(" + str(xi_pos) + "-x)*(x-" + str(xi) + "))"
        return solver_integral(integer_function, x_inf, x_sup, "0", "1", 10)
    else:
        x_inf = 0
        x_sup = 1
        if xi_pre > 0:
            x_inf = xi_pre
        if xi_pos < 1:
            x_sup = xi_pos
        
        if xi_pre > 1 or xi_pos < 0:
            return 0
        
        if xi>1:
            integer_function = "((1/(" + str(h**2)+ "))*((" + k_function + ") + ( " +  q_function + ")*((x-" + str(xi_pre) + ")**2)))"
            return solver_integral(integer_function, x_inf, x_sup, "0", "1", 10)
        else:
            first_integer_function = "((1/(" + str(h**2)+ "))*((" + k_function + ") + ( " +  q_function + ")*((x-" + str(xi_pre) + ")**2)))"
            second_integer_function = "((1/(" + str(h**2)+ "))*((" + k_function + ") + ( " +  q_function + ")*((" + str(xi_pos) +" - x)**2)))"

            first_solve = solver_integral(first_integer_function, x_inf, xi, "0", "1", 10)
            second_solve = solver_integral(second_integer_function, xi, x_sup, "0", "1", 10)

            return first_solve+second_solve


internal_multiplication(True, 0.7, 1.4, 2.1 , "x", "x", 0.7)