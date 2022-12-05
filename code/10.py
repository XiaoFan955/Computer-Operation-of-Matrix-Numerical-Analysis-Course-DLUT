# 《数值分析方法与应用》
#  第 214 页 插值与逼近 第1题


import numpy as np
import matplotlib.pylab as plt


# 定义插值函数f(x)
def inter_func(x):
    return 1/(1+x**2)


# 定义取[a,b]上步长为step的等距节点作为插值节点的lagrange插值多项式
def lagrange(a, b, step, x):
    x_list = np.arange(a,b,step)
    lag = 0
    for xi in x_list:
        lx = 1
        for xk in x_list:
            if  xk != xi:
                lx *= (x - xk) / (xi - xk)
        lag += inter_func(x) * lx
    return lag


# 数据部分
x1 = np.arange(-5,5+2,2)
y1 = lagrange(-5,5+2,2,x1)
x2 = np.arange(-5,5+1,1)
y2 = lagrange(-5,5+1,1,x2)
x3 = np.arange(-5,5+0.5,0.5)
y3 = lagrange(-5,5+0.5,0.5,x3)
x = np.arange(-5,5+0.001,0.001)
z = inter_func(x)

# 作图
fig = plt.figure()

font={
        'family':'Times New Roman',
        'weight':'light'
    }

plt.plot(x1,y1,"yellow")
plt.plot(x2,y2,"orange")
plt.plot(x3,y3,"red")
plt.plot(x,z,"green")
plt.title("lagrange")
plt.legend(['lagrange-step=2','lagrange-step=1','lagrange-step=0.5','$\mathdefault{f(x) \equal \\frac{1}{1+x^2}}$'],loc='upper left',prop=font)
plt.show()

