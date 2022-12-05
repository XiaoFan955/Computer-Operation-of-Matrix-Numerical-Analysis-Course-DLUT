# 《数值分析方法与应用》
#  第 214 页 非线性方程求解 第4题


# 定义迭代步数
STEP = 7
# 给定精确值
xx = 1


def newton_formula(x_cur):
    return x_cur - (pow(x_cur,3) + pow(x_cur,2) + x_cur -3) / (3 * pow(x_cur,2) + 2 * x_cur +1)


def computeNewton(formula, x0):
    x_next = x0
    e = []
    e.append(abs(x_next-xx))
    print("迭代第"+str(0)+"次, 初始值为: "+str(x_next)+", 绝对误差为"+str(e[0]))
    for i in range(1,8):
        x_cur = x_next
        x_next = formula(x_cur)
        e.append(abs(x_next-xx))
        print("迭代第"+str(i)+"次, 迭代结果为: "+str(x_next)+", 绝对误差为"+str(e[i])+", 与前一项误差平方比值为:"+str(e[i]/(e[i-1]**2)))


computeNewton(newton_formula, -0.7)