# 数值分析方法与应用》
# 第 214 页 插值与逼近 第5题


import numpy as np
import math
import matplotlib.pylab as plt


# 定义f(x)
def inter_func(x):
    return np.sin(x * math.pi)


# 计算均差
def computeDiffQuot(func,x_list):
    n = len(x_list)
    if n==1:
        return func(x_list[0])
    return (computeDiffQuot(func,x_list[1:n]) - computeDiffQuot(func,x_list[0:n-1])) / (x_list[n-1] - x_list[0])


# 插值函数为func,插值节点为x_list=[x0,x1,...,xn]的newton插值多项式
def newton(func,x_list,x):
    n = len(x_list)
    nt = 0
    for i in range(1,n):
        temp = 1
        for j in range(0,i-1):
            temp *= x - x_list[j]
        nt += temp * computeDiffQuot(func,x_list[0:i])
    nt += func(x_list[0])
    return nt


x = np.arange(0,1.1,0.1)
y = newton(inter_func,x,x)
x0 = np.arange(0,1,0.001)
z = inter_func(x0)


fig = plt.figure()

font={
        'family':'Times New Roman',
        'weight':'light'
    }


plt.plot(x,y,"red")
plt.plot(x0,z,"green")
plt.title("newton")
plt.legend(['newton-step=0.1','$\mathdefault{f(x) \equal \\sin{\pi x}}$'],loc='upper left',prop=font)# $\mathdefault{f(x) \equal \sin{\pi x}$
plt.show()