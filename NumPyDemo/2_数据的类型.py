import random

import numpy as np

# 创建numpy数组
t1 = np.array([1, 2, 3, 4, 5])
print(t1)
print(type(t1))
# 查看数据类型
print(t1.dtype)

# 设置数组类型
t2 = np.array([2, 3, 4, 5, 6], dtype='int32')
print(t2)
print(t2.dtype)

# 生成range数组
# t3 = np.array(range(5, 20, 4))
t3 = np.arange(5, 20, 4)
print(t3)
print(t3.dtype)
# 指定数组类型
t4 = np.asarray(t3, float, )
print(t4)
print(t4.dtype)

# 存储布尔类型
t5 = np.array([1, 0, 1, 0, 1, 0, 1, 1])
print(t5)
# 改变数组类型
t6 = t5.astype(dtype=bool)
print(t6)
print(type(t6))
print(t6.dtype)

# np中的小数
t7 = np.array([random.random() for i in range(5)])
# 四舍五入
t8 = np.round(t7,2)
print(t7)
print(t8)
