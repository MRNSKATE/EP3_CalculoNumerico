#Marco Antônio Rudas Napoli, n° USP: 11857970

from math import *

def value_function(function, x):
    new_function = eval(function)
    value = new_function

    return value

def transform_y(function, y_value):
    new_function = function.replace('y', y_value)
    return new_function

def nodules_analisys(n):
    if n == 6:
        x_j =  [0.2386191860831969086305017, 0.6612093864662645136613996, 0.9324695142031520278123016]
        w_j = [0.4679139345726910473898703, 0.3607615730481386075698335, 0.1713244923791703450402961]
    elif n== 8:
        x_j = [0.1834346424956498049394761, 0.5255324099163289858177390, 0.7966664774136267395915539, 0.9602898564975362316835609]
        w_j = [0.3626837833783619829651504, 0.3137066458778872873379622, 0.2223810344533744705443560, 0.1012285362903762591525314]
    else:
        x_j= [0.1488743389816312108848260,0.4333953941292471907992659, 0.6794095682990244062343274, 0.8650633666889845107320967, 0.9739065285171717200779640]
        w_j= [0.2955242247147528701738930, 0.2692667193099963550912269, 0.2190863625159820439955349, 0.1494513491505805931457763, 0.0666713443086881375935688]
    
    x_j_copy = x_j.copy()
    w_j_copy = w_j.copy()
    for i in range(len(x_j)):
        index = -1-i
        x_j_copy.append((x_j[index])*(-1))
        w_j_copy.append(w_j[index])
    x_j=x_j_copy
    w_j=w_j_copy
        
    return x_j, w_j


def solver_integral(function, x_inf, x_sup, y_inf, y_sup, n):
    x_j, w_j = nodules_analisys(n)
    total_value = 0
    c = (x_sup - x_inf)/2
    d = (x_sup + x_inf)/2
    for i in range(len(x_j)):
        for j in range(len(x_j)):
            x_x_i = c*x_j[j] + d
            new_ysup_value = value_function(y_sup, x_x_i)
            new_yinf_value = value_function(y_inf, x_x_i)
            y_x_i = (1/2)*(((new_ysup_value - new_yinf_value)*x_j[i])+(new_ysup_value + new_yinf_value))
            new_function = '(('+str(y_sup)+'-'+ str(y_inf) +')/2)'+'*'+str(w_j[i])+'*('+transform_y(function, str(y_x_i))+')'
            x_new_function = value_function(new_function, x_x_i)*((x_sup-x_inf)/2)*w_j[j]
            total_value = total_value + x_new_function
    return total_value

solver_integral("x+y", 0, 2, "x", "2*x", 8)
