import numpy as np

# 创建一维数组
t1 = np.arange(12)
print(t1)
# 查看形状
print(t1.shape)

# 创建二维数组
t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2)
# 查看形状
print(t2.shape)

# 创建三维数组
t3 = np.array([[[1, 2, 3], [4, 5, 6]], [[4, 5, 6], [7, 8, 9]]])
print(t3)
print(t3.shape)

# 一维转二维
t4 = np.arange(12)
t5 = t4.reshape((3, 4))
print(t5)

# 一维转三维
t6 = np.arange(24).reshape((2, 3, 4))
print(t6)

# 三维转二维
t7 = t6.reshape((3, 8))
print(t7)

# 三维转一维，二维转一维同理
t8 = t6.reshape((24,))
print(t8)

# 多维转一维，将多维数组展开，flatten--展开
t9 = t3.flatten()
print(t9)
