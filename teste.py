from math import *
from cmath import cos, pi
import numpy as np

from SolverIntegralByString import *
from SolverTridiagonalSystem import *

f_function = str(input("Digite a função f(x) da sua equação diferencial: "))
k_function = str(input("Digite a função k(x) da sua equação diferencial: "))
q_function = str(input("Digite a função q(x) da sua equação diferencial: "))

print("Agora iremos analisar o intervalo em que a solução será proposta:")
u_inf_value = float(input("Digite o intervalo inferior da função u(x): "))
u_sup_value = float(input("Digite o intervalo superior da função u(x): "))

number_analysis = int(input("Digite o número de subdivisões que você gostaria de analisar: "))

def internal_multiplication_hat(equal, xi_pre, xi, xi_pos, h, k_function, q_function):
    #Quando os valores do chapéu forem iguais
    if equal == 0:
        first_integer = '(' + str((1/h)**2) + '*(' + k_function + '))'
        second_integer = '(' + str((-1/h)**2) + '*(' + k_function + '))'
        third_integer = '(' + str((1/h)**2) + '*((x-' + str(xi_pre) +')**2)*(' + q_function + '))'
        fourth_integer = '(' + str((1/h)**2) + '*(('+ str(xi_pos) + '-x)**2)*(' + q_function + '))'

        total_value = solver_integral(first_integer, xi_pre, xi, '0', '1', 6) + solver_integral(second_integer, xi, xi_pos, '0', '1', 6) + solver_integral(third_integer, xi_pre, xi, '0', '1', 6) + solver_integral(fourth_integer, xi, xi_pos, '0', '1', 6)
        return total_value
    
    #Quando for para a diagonal ai,i+1:
    elif equal == 1:
        first_integer = '(' + str(-((1/h)**2)) + '*(' + k_function + '))'
        second_integer = '(' + str((1/h)**2) + '*(('+ str(xi_pos) + '- x) * (x - ' + str(xi) + '))*(' + q_function +'))'

        total_value = solver_integral(first_integer, xi, xi_pos, '0', '1', 6) + solver_integral(second_integer, xi, xi_pos, '0', '1', 6)
        return total_value
    
    elif equal == 2:
        first_integer = '(' + str(-((1/h)**2)) + '*(' + k_function + '))'
        second_integer = '(' + str((1/h)**2) + '*(('+ str(xi) + '- x) * (x - ' + str(xi_pre) + '))*(' + q_function +'))'

        total_value = solver_integral(first_integer, xi_pre, xi, '0', '1', 6) + solver_integral(second_integer, xi_pre, xi, '0', '1', 6)
        return total_value

def internal_multiplication_function(xi_pre, xi, xi_pos, h, f_function):
    first_integer = '('+ str(1/h)+'*(x-'+ str(xi_pre) + ')*'+ f_function +')'
    second_integer = '('+ str(1/h)+'*('+str(xi_pos) + '- x )*'+ f_function +')'

    total_value = solver_integral(first_integer, xi_pre, xi, '0', '1', 6) + solver_integral(second_integer, xi, xi_pos, '0', '1', 6)
    return total_value

#Consrtrução do vetor b
h = (u_sup_value-u_inf_value)/(number_analysis+1)

#Mapeando o produto interno do vetor b:
b_vector = []
for i in range(number_analysis):
    xi_pre = i*h
    xi = xi_pre + h
    xi_pos = xi + h

    value = internal_multiplication_hat(0, xi_pre, xi, xi_pos, h, k_function, q_function)

    b_vector.append(value)

#Mapeando o produto interno do vetor c:
c_vector = []
for i in range(number_analysis):
    xi_pre = i*h
    xi = xi_pre + h
    xi_pos = xi + h

    value = internal_multiplication_hat(1, xi_pre, xi, xi_pos, h, k_function, q_function)

    c_vector.append(value)
c_vector.append(0)

#Mapeando o produto interno do vetor a:
a_vector = [0]
xi_control = []
for i in range(number_analysis):
    xi_pre = i*h
    xi = xi_pre + h
    xi_pos = xi + h

    value = internal_multiplication_hat(2, xi_pre, xi, xi_pos, h, k_function, q_function)

    a_vector.append(value)
    xi_control.append(xi_pre)

    if i == (number_analysis-1):
        xi_control.append(xi)
        xi_control.append(xi_pos)

print(b_vector)
print(c_vector)
print(a_vector)

#Mapeando o produto interno do vetor d:
d_vector = []
for i in range(number_analysis):
    xi_pre = i*h
    xi = xi_pre + h
    xi_pos = xi + h

    value = internal_multiplication_function(xi_pre, xi, xi_pos, h, f_function)

    d_vector.append(value)

print(d_vector)
print(xi_control)
initial_solution(a_vector, b_vector, c_vector, d_vector, number_analysis)