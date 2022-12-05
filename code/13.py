# 《数值分析方法与应用》
#  第 214 页 数值积分 第2题


import numpy as np
import math
from scipy.special import roots_legendre
from sympy import *


# 定义积分函数f(x)
def integ_func(x):
    return x**2 * np.cos(x)


# 使用gauss-Legendre公式求积
def gaussLegendre(func,a,b,n):
    x,w = roots_legendre(n)
    xp = x*(b-a)/2+(b+a)/2
    wp = w*(b-a)/2
    ans = 0
    for i in range(0, n):
        ans += wp[i] * func(xp[i])
    return ans

a = 0
b = math.pi/2
print("2点Gauss型积分结果为: " + str(gaussLegendre(integ_func,a,b,2)))
print("3点Gauss型积分结果为: " + str(gaussLegendre(integ_func,a,b,3)))
print("5点Gauss型积分结果为: " + str(gaussLegendre(integ_func,a,b,5)))


# 真实值
x = symbols('x')
y = x**2*cos(x)
print("真实值: " + str(integrate(y, (x, 0, math.pi/2)))) 