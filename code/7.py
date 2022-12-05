# 《数值分析方法与应用》
#  第 214 页 线性方程组求解 第6题


import numpy as np


# 生成n阶Hilbert矩阵
def genHilbert(n):
    H = np.mat(np.zeros((n,n)))
    for i in range(0,n):
        for j in range(0,n):
            H[i,j] = 1 / (i + j +1)
    return H


# LU分解,根据书P37公式
def doolittle(A:np.matrix):
    n = A.shape[0]
    L = np.mat(np.zeros((n,n)))
    U = np.mat(np.zeros((n,n)))
    for i in range(0,n):
        L[i,i] = 1
    for j in range(0,n):
        U[0,j] = A[0,j]
    for j in range(1,n):
        L[j,0] = A[j,0]/U[0,0]
    for i in range(1,n):
        for j in range(i,n):
            sum = 0
            for k in range(0,i):
                sum += L[i,k] * U[k,j]
            U[i,j] = A[i,j] - sum
            if i != j:
                sum = 0
                for k in range(0,i):
                    sum += L[j,k] * U[k,i]
                L[j,i] = (A[j,i] - sum)/U[i,i]
    return L,U


# Gauss消去法求解方程组(回代法)
def gaussCompute(A:np.matrix,b:np.matrix):
    n = A.shape[0]
    x = np.mat(np.zeros((n,1)))
    L,U = doolittle(A)
    Lb = np.linalg.inv(L) * b
    for i in reversed(range(0,n)):
        sum = 0
        for k in range(i+1,n):
            sum += U[i,k] * x[k,0]
        x[i,0] = (Lb[i,0] - sum) / U[i,i]
    return x


# n=2情形
H = genHilbert(2)
b = np.mat(np.ones((2,1)))
print("n=2, 解得x=" + str(gaussCompute(H,b)))

# n=5情形
H = genHilbert(5)
b = np.mat(np.ones((5,1)))
print("n=5, 解得x=" + str(gaussCompute(H,b)))

# n=10情形
H = genHilbert(10)
b = np.mat(np.ones((10,1)))
print("n=10, 解得x=" + str(gaussCompute(H,b)))