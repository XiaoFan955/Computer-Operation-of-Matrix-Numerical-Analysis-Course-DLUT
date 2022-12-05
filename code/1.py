# 《计算机科学计算》第二版 张宏伟等 编著 高等教育出版社
# 第 162 页 第四章课后习题第 12 (1)题


# 定义精度
BOUND = 1e-5


# newton迭代式
def newton_formula(x_cur):
    return x_cur - (pow(x_cur,3) + pow(x_cur,2) + x_cur + 1) / (3 * pow(x_cur,2) + 2 * x_cur +1)


# 迭代计算
def computeNewton(formula, x0):
    x_cur = x0
    x_next = formula(x_cur)
    count = 1
    while(abs(x_next - x_cur) >= BOUND):
        count+=1
        x_cur = x_next
        x_next = formula(x_cur)
    print("迭代"+str(count)+"次，求得根为: "+str(x_next))


# 迭代初值
x0 = 2.0


computeNewton(newton_formula, x0)