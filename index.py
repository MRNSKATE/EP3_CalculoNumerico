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

# inicialmente consideraremos x pertence a (0, 1) com u(0) = u(1) = 0
def internal_multiplication(u_function, xi_u, v_function, xi_v, k_function, q_function, h):
    print("Desenvolvendo")
    if u_function != v_function:
        if xi_u[0] < xi_v[0]:
            """pre_function = u_function
            pre_xi = xi_u
            pos_function = v_function
            pos_xi = xi_v
            x_inf = 0
            x_sup = 1
            if pre_xi[0] > 0:
                x_inf = pre_xi[0]
            if pos_xi[2] < 1:
                x_sup = pos_xi[2]"""
            u_linha = str(1/h)
            v_linha = str(-1/h)
            integer_function = "2*(((" + k_function + ")*("+ulinha+")*("+v_linha+"))"+"(("+q_function+")*"+u_function+")*("+v_function+"))"+")"

            value = solver_integral(integer_function, 0, 1, "0", "1", 10)
            print(value)
def homogeneous_fronteir(f_function, k_function, q_function, number_analysis):
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
        
        integer_inf = solver_integral("("+f_function+")*("+chapeu_one_line+")", xi_pre, xi, "0", "1", 10)
        integer_sup = solver_integral("("+f_function+")*("+chapeu_two_line+")", xi, xi_pos, "0", "1", 10)

        range_control.append(xi_pre)
        if i == number_analysis - 1:
            range_control.append(xi)
            range_control.append(xi_pos)

        d_vector.append(integer_inf+integer_sup)

    #Resolução do sistema tridiagonal e descoberta dos coeficientes de Un(x) = sum(alfa*chapéu)
    initial_solution(a_vector, b_vector, c_vector, d_vector, number_analysis)
    print(range_control)

def no_homogeneous_fronteir(f_function, k_function, q_function, u_inf_value, u_sup_value, number_analysis):
    k_derivative = str(input("Digite a derivada da função k(x): "))
    new_f_function = f_function + "+" + str(u_sup_value-u_inf_value) + "*" + k_derivative + "-" + q_function + "*(" + str(u_inf_value) + "+ x*(" + str(u_sup_value-u_inf_value) + "))"
    
    h = 1/(number_analysis+1)

    for i in range(number_analysis):
        xi_pre = i*h
        xi = xi_pre + h
        xi_pos = xi + h
        chapeu_one_line = "(x-"+str(xi_pre)+")/"+str(h)
        chapeu_two_line = "("+str(xi_pos)+"-x)/"+str(h)

if u_inf_value == 0 and u_sup_value == 1:
    homogeneous_fronteir(f_function, k_function, q_function, number_analysis)
else:
    no_homogeneous_fronteir(f_function, k_function, q_function, u_inf_value, u_sup_value, number_analysis)
