import random

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
y_1 = [24, 28, 21, 23, 18, 23, 35, 31, 29, 27, 27, 26, 27, 33, 33, 33, 29, 31, 23, 26, 28, 28, 32, 35, 25, 22, 21, 31,
       31, 34, 31, 31]
y_2 = [29, 31, 23, 26, 22, 28, 34, 37, 32, 37, 31, 26, 33, 29, 32, 35, 32, 33, 33, 24, 26, 28, 26, 20, 20, 25, 36, 30,
       20, 26, 23, 23]
x_1 = range(32)
x_2 = range(51, 83)

plt.figure(figsize=(16, 8), dpi=100)

plt.scatter(x_1, y_1,label='3月份')
plt.scatter(x_2, y_2,label='10月份')

# 调整x轴刻度

_x = list(x_1) + list(x_2)
_xtick_lables = ['3月{}日'.format(i) for i in x_1]
_xtick_lables += ['10月{}日'.format(i - 50) for i in x_2]
plt.xticks(_x[::3], _xtick_lables[::3], rotation=45)

# 添加图例
plt.legend()

# 添加描述信息
plt.title('3月与10月温度变化图')
plt.xlabel('日期')
plt.ylabel('摄氏度 ℃')

plt.show()
