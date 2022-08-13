import numpy as np

t1 = np.array([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]])
# 矩阵的加法
t2 = t1 + 2
# 矩阵的减法
t3 = t1 - 2
# 矩阵的乘法
t4 = t1 * 2
# 矩阵的除法
t5 = t1 / 2
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)

# 矩阵与矩阵计算
# 3 x 4 的矩阵
t6 = np.arange(110, 122).reshape((3, 4))
# 矩阵的加法
t7 = t1 + t6
# 矩阵的减法和上面相同.....
print(t6)
print(t7)

t8 = np.arange(3).reshape((3,1))
print(t8)
t9 = t7-t8
print(t9)

