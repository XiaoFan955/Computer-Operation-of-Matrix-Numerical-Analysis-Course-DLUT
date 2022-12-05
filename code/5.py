# 《数值分析方法与应用》
#  第 214 页 基础知识部分 第5题


import numpy as np
import matplotlib.pylab as plt


# 秦九韶算法计算多项式通用程序
# v: 系数列表,高次到低次,
# x: 计算点x0
def qinJiuShao(v,x):
    if len(v) == 0:
        return 0
    ans = v[0];
    for i in range(1,len(v)):
        ans = ans * x + v[i]
    return ans


# 数据部分
v = [1,-18,144,-672,2016,-4032,5376,-4608,2304,-512]
x = np.arange(1.95,2.06,0.01)
y = qinJiuShao(v,x)


# 作图
plt.plot(x,y,"-p")
plt.title("$(x-2)^9$")
for xi,yi in zip(x,y):
    plt.text(xi, yi-2e-12, "(" + '%.2f' %xi + "," + '%.12f' % yi + ")", ha='center', va= 'bottom',fontsize=9)
plt.ylim(-2e-11,2e-11)
plt.show()

