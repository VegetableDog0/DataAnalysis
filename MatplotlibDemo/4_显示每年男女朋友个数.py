import random

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

x = range(11, 31)
y_1 = [random.randint(1, 10) for i in range(31+1)]  # 自己的女朋友个数
y_2 = [random.randint(1, 10) for j in range(31+1)]  # 同桌的女朋友个数

plt.figure(figsize=(12, 8), dpi=80)
plt.plot(x, y_1, label='自己', color='orange', linestyle=':', linewidth=5,alpha=0.8)  # 设置图例名、线条颜色、线型、宽度
plt.plot(x, y_2, label='同桌', color='#4B0082', linestyle='--')  # 设置图例名、十六进制颜色
_yticks_label = ['{}个'.format(i) for i in range(1, 11)]
_xticks_label = ['{}岁'.format(i) for i in x]
plt.xticks(list(x)[::1], _xticks_label[::1])  # 设置x轴显示字符串
plt.yticks(list(range(1, 11))[::1], _yticks_label[::1])  # 设置y轴显示字符串
# 显示网格
plt.grid(alpha=0.4, linestyle='-.')
# 添加图例名
plt.legend(loc=3)

plt.show()
