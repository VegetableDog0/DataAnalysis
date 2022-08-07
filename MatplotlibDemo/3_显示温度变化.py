import random

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 设置图片大小
# figure是图片图标的意思，这里指我们绘制的图
# dpi则是在屏幕上的分辨率
fig = plt.figure(figsize=(14, 8), dpi=80)

x = range(0, 121)
y = [random.randint(20, 38) for i in range(121)]

# 绘制图片
plt.plot(x, y)
# 调整x轴刻度
_xticks_labelz = ['10点{}分'.format(i) for i in range(60)]
_xticks_labelz += ['11点{}分'.format(i) for i in range(61)]
# 去步长，数字和字符串的个数一一对应，数据的长度一样
plt.xticks(list(x)[::3], _xticks_labelz[::3], rotation=45)  # rotation设置旋转多少度
plt.xlabel('时间')  # 设置x轴名称
plt.ylabel('温度 单位(℃)')  # 设置y轴名称
plt.title('10点到12点气温变化图')  # 设置标题名称
# 展示图片
plt.show()
