# 《数值分析方法与应用》
#  第 214 页 基础知识部分 第1题


import numpy as np


# N从小到大计算
def func_SN(n):
    sum = 0
    for i in range(2,n+1):
        sum += np.float32(1/((pow(i,2))-1))
        sum = np.float32(sum)
    return np.float32(sum)


# N从大到小计算
def func_SN_reverse(n):
    sum = 0
    for i in range(2,n+1):
        sum += np.float32(1/((pow(n+2-i,2))-1))
        sum = np.float32(sum)
    return np.float32(sum)


# 精确值
def exactval(n):
    return (((((3 / 2) - (1 / n)) - (1 / (n+1)))) / 2)


# 计算有效数字 significant digits
def getSD(x,a):
    e = abs(x - a)
    a = abs(a)
    n = 0
    while(a > 1):
        a /= 10
        n +=1
    while(e < 0.05):
        n += 1
        e *= 10
    return n


sn0 = exactval(pow(10,2))
sn1 = func_SN(pow(10,2))
sn2 = func_SN_reverse(pow(10,2))
print("N=10^2:")
print(" 精确值 计算结果:" + str(sn0))
print("从大到小计算结果:" + str(sn1))   # + ", 有效数字为: n=" + str(getSD(sn0,sn1))
print("从小到大计算结果:" + str(sn2))   # + ", 有效数字为: n=" + str(getSD(sn0,sn2))

sn0 = exactval(pow(10,4))
sn1 = func_SN(pow(10,4))
sn2 = func_SN_reverse(pow(10,4))
e1 = abs(sn0 - sn1)
e2 = abs(sn0 - sn2)
print("N=10^4:")
print(" 精确值 计算结果:" + str(sn0))
print("从大到小计算结果:" + str(sn1))
print("从小到大计算结果:" + str(sn2))


sn0 = exactval(pow(10,6))
sn1 = func_SN(pow(10,6))
sn2 = func_SN_reverse(pow(10,6))
e1 = abs(sn0 - sn1)
e2 = abs(sn0 - sn2)
print("N=10^6:")
print(" 精确值 计算结果:" + str(sn0))
print("从大到小计算结果:" + str(sn1))
print("从小到大计算结果:" + str(sn2))
