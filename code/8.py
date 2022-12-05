# 《数值分析方法与应用》
#  第 214 页 非线性方程求解 第1题


import math

# 定义精度
BOUND = 1e-5


# 第一个方程的newton迭代公式
def newton_formula1(x_cur):
    return x_cur - (2 * pow(x_cur,3) - 5 * x_cur + 1) / (6 * pow(x_cur,2) - 5)


# 第一个方程的割线法迭代公式
def secant_formula1(x_pre, x_cur):
    return x_cur - (2 * pow(x_cur,3) - 5 * x_cur + 1) * (x_cur - x_pre) / ((2 * pow(x_cur,3) - 5 * x_cur + 1) - (2 * pow(x_pre,3) - 5 * x_pre + 1))


# 第二个方程的newton迭代公式
def newton_formula2(x_cur):
    return x_cur - (math.exp(x_cur) * math.sin(x_cur)) / (math.exp(x_cur) * (math.sin(x_cur) + math.cos(x_cur)))


# 第二个方程的割线法迭代公式
def secant_formula2(x_pre, x_cur):
    return x_cur - (math.exp(x_cur) * math.sin(x_cur)) * (x_cur - x_pre) / ((math.exp(x_cur) * math.sin(x_cur)) - (math.exp(x_pre) * math.sin(x_pre)))


# newton迭代法计算
def computeNewton(formula, x0):
    x_cur = x0
    x_next = formula(x_cur)
    count = 1
    while(abs(x_next - x_cur) > BOUND):
        count += 1
        x_cur = x_next
        x_next = formula(x_cur)
    print("经过"+str(count)+"轮迭代，求得根为: "+str(x_next))


# 割线法计算
def computeSecant(formula, x0, x1):
    x_pre = x0
    x_cur = x1
    x_next = formula(x_pre, x_cur)
    count = 1
    while(abs(x_next - x_cur) > 0):
        count += 1
        x_pre = x_cur
        x_cur = x_next
        x_next = formula(x_pre, x_cur)
    print("经过"+str(count)+"轮迭代，求得根为: "+str(x_next))


print("方程(1), Newton法迭代结果: ")
computeNewton(newton_formula1, 1.5)
print("方程(1), 割线法迭代结果: ")
computeSecant(secant_formula1, 1, 2)
print("方程(2), Newton法迭代结果: ")
computeNewton(newton_formula2, -3.5)
print("方程(2), 割线法迭代结果: ")
computeSecant(secant_formula2, -4, -3)