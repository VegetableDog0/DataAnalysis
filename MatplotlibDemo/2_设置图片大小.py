from matplotlib import pyplot as plt

# 设置图片大小
# figure是图片图标的意思，这里指我们绘制的图
# dpi则是在屏幕上的分辨率
fig = plt.figure(figsize=(20, 8), dpi=80)

x = range(2, 26, 2)
y = [6, 5, 8, 4, 1, 1, 6, 2, 8, 5, 8, 7]

# 绘制图片
plt.plot(x, y)
# 设置刻度
plt.xticks(x)  # x Axis的刻度
# plt.xticks(x[::2])  # 当x轴比较稀疏时，可以设置步长进行显示（间隔取值）
plt.yticks(range(min(y), max(y)+1))  # y Axis的刻度
# 保存图片，在图片绘制之后才能保存，不然是空白
plt.savefig('./img/figure_size.png')
# 展示图片
plt.show()
