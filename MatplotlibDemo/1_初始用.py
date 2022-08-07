from matplotlib import pyplot as plt

# 数据在x轴的位置，是一个可迭代的对象
x = range(2, 26, 2)
# 数据在y轴的位置，是一个可迭代的对象
y = [6, 5, 8, 4, 1, 1, 6, 2, 8, 5, 8, 7]
# 在图中的则表示为（2，6）,(4,5),(6,8)....(24,7)
# 传入x，y，绘制出图像
plt.plot(x, y)
# 显示出图像
plt.show()
