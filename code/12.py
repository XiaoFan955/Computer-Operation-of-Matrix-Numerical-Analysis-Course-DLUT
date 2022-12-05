# 《数值分析方法与应用》
#  第 214 页 插值与逼近 第7题
""" 
先写出λ、μ、g等的初值(第二类边界条件)
构造三对角矩阵求解m0~mn
得出m0~mn的值后, 根据x的范围选择m写出对应的分段函数
带入x求值
"""
import numpy as np


# 计算hk, k = 0,1,2,...,n-1
def h(x,k):
    return x[k+1] - x[k]


# 计算λ、μ、g等的初值
# 计算λ的初值, k = 1,2,...,n-1
def getLambda(x,k):
    return h(x,k) / (h(x,k) + h(x,k-1))


# 计算μ的初值, k = 1,2,...,n-1
def getMiu(x,k):
    return h(x,k-1) / (h(x,k) + h(x,k-1))


# 计算g的初值, k = 0,1,2,...,n
def getG(x,y,k,sSd0,sSdn):
    n = len(x)
    if k == 0:
        return 3 * (y[1] - y[0]) / h(x,0) - h(x,0) * sSd0 / 2
    if k == n-1:
        return 3 * (y[n-1] - y[n-2]) / h(x,n-2) - h(x,n-2) * sSdn / 2
    return 3 * (getMiu(x,k) * (y[k+1] - y[k]) / h(x,k) + getLambda(x,k) * (y[k] - y[k-1]) / h(x,k-1))


# 返回三对角矩阵和g向量
def initSplineIntp(x,y,sSd0,sSdn):
    n = len(x)
    g = []
    for k in range(0,n):
         g.append(getG(x,y,k,sSd0,sSdn))
    A = np.mat(np.zeros((n,n)))
    A[0,1] = 1
    A[n-1,n-2] = 1
    for i in range(0,n):
        A[i,i] = 2
        if i >= 1 and i < n - 1:
            A[i,i-1] = getLambda(x,i)
            A[i,i+1] = getMiu(x,i)
    return A,g


# 求三对角矩阵的LU分解, 书P49
def doolittleForTriMat(A):
    n = A.shape[0]
    L = np.mat(np.zeros((n,n)))
    U = np.mat(np.zeros((n,n)))
    U[0,0] = A[0,0]
    for i in range(0,n-1):
        U[i,i+1] = A[i,i+1]
    for i in range(1,n):
        L[i,i-1] = A[i,i-1] / U[i-1,i-1]
        U[i,i] = A[i,i] - L[i,i-1] * A[i-1,i]
    return L,U


# 追赶法求三对角矩阵, 书P49
def computeTriMat(A,g):
    n = A.shape[0]
    L,U = doolittleForTriMat(A)
    y = np.mat(np.zeros((n,1)))
    m = np.mat(np.zeros((n,1)))
    y[0,0] = g[0]
    for i in range(1,n):
        y[i,0] = g[i] - L[i,i-1] * y[i-1,0]
    m[n-1,0] = y[n-1,0] / U[n-1,n-1]
    for i in reversed(range(0,n-2)):
        m[i,0] = (y[i,0] - U[i,i+1] * m[i+1,0]) / U[i,i]
    return m


# 确定x在哪个插值区间
def getX_index(x_list,x):
    n = len(x_list)
    for i in range(0,n-1):
        if x >= x_list[i] and x <= x_list[i+1]:
            return i
    return n-1


# 样条插值函数
def excSplineIntp(x_list,y,sSd0,sSdn,x):
    A,g = initSplineIntp(x_list,y,sSd0,sSdn)
    m = computeTriMat(A,g)
    k = getX_index(x_list,x)
    return (h(x_list,k) + 2 * (x - x_list[k])) * pow(x - x_list[k+1],2) * y[k] / pow(h(x_list,k),3) + (h(x_list,k) - 2 * (x - x_list[k+1])) * pow(x - x_list[k],2) * y[k+1] / pow(h(x_list,k),3) + (x - x_list[k]) * pow(x - x_list[k],2) * m[k] / pow(h(x_list,k),2) + (x - x_list[k+1]) * pow(x - x_list[k],2) * m[k+1] / pow(h(x_list,k),2)



# 样条节点与对应的函数值
x = [0,1,2,3,4]
s = [1,3,3,4,2]
# 边界条件 Sd: second derivative
sSd0 = 0
sSd4 = 0


A,g = initSplineIntp(x,x,sSd0,sSd4)
m = computeTriMat(A,g)
print("m的值为: " + str(computeTriMat(A,g)))