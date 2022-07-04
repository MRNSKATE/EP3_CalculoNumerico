from math import *
from cmath import cos, pi
import numpy as np

from SolverIntegralByString import *
from SolverTridiagonalSystem import *

q_function = str(input("Digite a função Q(x) da sua equação diferencial: "))

# inicialmente consideraremos x pertence a (0, 1) com u(0) = u(1) = 0

number_analysis = int(input("Digite o número de subdivisões que você gostaria de analisar: "))

h = 1/(number_analysis+1)
#Formação dos vetores que participarão do sistema tridiagonal 
b_vector = []
for i in range(number_analysis):
    b_vector.append(2/h)

a_vector = [0]
for i in range(number_analysis-1):
    a_vector.append(-1/h)

c_vector = []
for i in range(number_analysis-1):
    c_vector.append(-1/h)
c_vector.append(0)

#Cálculo dos produtos iternos entre Q(x) e a função chapéu
range_control = []
d_vector = []
for i in range(number_analysis):
    xi_pre = i*h
    xi = xi_pre + h
    xi_pos = xi + h
    chapeu_one_line = "(x-"+str(xi_pre)+")/"+str(h)
    chapeu_two_line = "("+str(xi_pos)+"-x)/"+str(h)
    
    integer_inf = solver_integral(q_function+"*"+chapeu_one_line, xi_pre, xi, "0", "1", 10)
    integer_sup = solver_integral(q_function+"*"+chapeu_two_line, xi, xi_pos, "0", "1", 10)

    range_control.append(xi_pre)
    if i == number_analysis - 1:
        range_control.append(xi)
        range_control.append(xi_pos)

    d_vector.append(integer_inf+integer_sup)

#Resolução do sistema tridiagonal e descoberta dos coeficientes de Un(x) = sum(alfa*chapéu)
initial_solution(a_vector, b_vector, c_vector, d_vector, number_analysis)
print(range_control)