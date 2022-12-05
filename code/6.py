# 《数值分析方法与应用》
#  第 214 页 线性方程组求解 第2题


import numpy as np
import math


# 判断是否对称
def checkSym(A:np.matrix):
    n = A.shape[0]
    for i in range(0,n):
        for j in range(i+1,n):
            if A[i,j] != A[j,i]:
                return False
    return True


# 判断是否正定
def checkPos(A:np.matrix):
    return np.all(np.linalg.eigvals(A)>0)


# cholesky算法,根据书P46公式
def cholesky(A:np.matrix):
    n = A.shape[0]
    L = np.mat(np.zeros((n,n)))
    for j in range(0,n):
        sum = 0
        for k in range(0,j):
            sum += L[j,k] ** 2
        L[j,j] = math.sqrt(A[j,j] - sum)
        for i in range(j+1,n):
            sum = 0
            for k in range(0,j):
                sum += L[i,k] * L[j,k]
            L[i,j] = (A[i,j] - sum)/L[j,j]
    return L


# cholesky分解求解线性方程组
def choleskyCompute(A:np.matrix,b:np.matrix):
    if not (checkPos(A) and checkSym(A)):
        print("矩阵A不是对称正定矩阵!")
        return
    L = cholesky(A)
    n = A.shape[0]
    y = np.mat(np.zeros((n,1)))
    x = np.mat(np.zeros((n,1)))
    y[0,0] = b[0,0]/L[0,0]
    for i in range(1,n):
        sum = 0
        for k in range(0,i):
            sum += L[i,k] * y[k,0]
        y[i,0] = (b[i,0] - sum)/L[i,i]
    x[n-1,0] = y[n-1,0]/L[n-1,n-1]
    for i in reversed(range(0,n-1)):
        sum = 0
        for k in range(i,n):
            sum += L[k,i] * x[k,0]
        x[i,0] = (y[i,0] - sum)/L[i,i]
    return x


A = np.matrix([[7,1,-5,1],[1,9,2,7],[-5,2,7,-1],[1,7,-1,9]])
b = np.matrix([[13],[-9],[6],[0]])
print("求得解向量x="+str(choleskyCompute(A,b)))