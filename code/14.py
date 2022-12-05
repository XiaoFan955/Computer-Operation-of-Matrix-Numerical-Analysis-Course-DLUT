# 《数值分析方法与应用》
#  第 214 页 微分方程数值解法 第1题


import math
import numpy as np
import matplotlib.pylab as plt

# f(u,t)
def f(u,t):
    return 2 * u / t + t ** 2 * math.exp(t)


# Euler法
def euler(a,b,h,f,u0):
    u = []
    u.append(u0)
    t = np.arange(a,b,h)
    n = t.shape[0]
    for i in range(0,n):
        u.append(u[i] + h * f(u[i],t[i]))
    return u


# 改进的Euler法
def improvedEuler(a,b,h,f,u0):
    u = []
    u.append(u0)
    t = np.arange(a,b+h,h)
    n = t.shape[0]
    for i in range(0,n-1):
        u.append(u[i] + h / 2 * (f(u[i],t[i]) + f(u[i] + h * f(u[i],t[i]),t[i+1])))
    return u


# Runge-Kutta法 m=4
def rungeKutta(a,b,h,f,u0):
    u = []
    u.append(u0)
    t = np.arange(a,b+h,h)
    n = t.shape[0]
    for i in range(0, n - 1):
        k1 = f(u[i], t[i])
        k2 = f(u[i] + h * k1 / 2, t[i] + h / 2)
        k3 = f(u[i] + h * k2 / 2, t[i] + h / 2)
        k4 = f(u[i] + h * k3, t[i] + h)
        u.append(u[i] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
    return u


# 初始数据
a = 1
b = 2
h = [0.1,0.05,0.01]
u0 = 0


# 作图
fig = plt.figure()
font={
        'family':'Times New Roman',
        'weight':'light'
    }
plt.subplot(1,3,1)
x = np.arange(a,b+h[0],h[0])
y = euler(a,b,h[0],f,u0)
plt.plot(x,y,"green")
x = np.arange(a,b+h[1],h[1])
y = euler(a,b,h[1],f,u0)
plt.plot(x,y,"orange")
x = np.arange(a,b+h[2],h[2])
y = euler(a,b,h[2],f,u0)
plt.plot(x,y,"red")
plt.title("Euler")
plt.legend(['step=0.1','step=0.05','step=0.01'],loc='upper left',prop=font)


plt.subplot(1,3,2)
x = np.arange(a,b+h[0],h[0])
y = improvedEuler(a,b,h[0],f,u0)
plt.plot(x,y,"green")
x = np.arange(a,b+h[1],h[1])
y = improvedEuler(a,b,h[1],f,u0)
plt.plot(x,y,"orange")
x = np.arange(a,b+h[2],h[2])
y = improvedEuler(a,b,h[2],f,u0)
plt.plot(x,y,"red")
plt.title("improved-Euler")
plt.legend(['step=0.1','step=0.05','step=0.01'],loc='upper left',prop=font)


plt.subplot(1,3,3)
x = np.arange(a,b+h[0],h[0])
y = rungeKutta(a,b,h[0],f,u0)
plt.plot(x,y,"green")
x = np.arange(a,b+h[1],h[1])
y = rungeKutta(a,b,h[1],f,u0)
plt.plot(x,y,"orange")
x = np.arange(a,b+h[2],h[2])
y = rungeKutta(a,b,h[2],f,u0)
plt.plot(x,y,"red")
plt.title("Runge-Kutta")
plt.legend(['step=0.1','step=0.05','step=0.01'],loc='upper left',prop=font)
plt.show()