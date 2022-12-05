# 《计算机科学计算》第二版 张宏伟等 编著 高等教育出版社
# 第 216 页 第六章课后习题第 12 题


import math


# 椭圆周长近似公式
def ellipseCirc(a,b):
    return math.pi * (1.5 * (a + b) - math.sqrt(a * b))


a = 8755
b = 6810
print("轨道周长为: "+str(ellipseCirc(a,b)))