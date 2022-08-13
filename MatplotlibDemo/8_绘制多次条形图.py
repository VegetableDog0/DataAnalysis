from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
x = ['长津湖', '战狼2', '你好，李焕英']
y_1 = [577523, 569454, 541308, ]
y_2 = [541308, 503570, 468674, ]
y_3 = [468674, 452341, 425013, ]

# 设置条形图宽度
# bar_width = 0.1
bar_width = 0.2
# bar_width = 0.3

# 根据条形图宽度进行确定x的宽度
x_1 = list(range(len(x)))
x_2 = [i + bar_width for i in x_1]
x_3 = [i + bar_width * 2 for i in x_1]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=100)
plt.bar(range(len(x)), y_1, width=bar_width, label='9月')
plt.bar(x_2, y_2, width=bar_width, label='10月')
plt.bar(x_3, y_3, width=bar_width, label='11月')

# 设置x轴刻度
plt.xticks(x_2, x)

plt.title('电影统计')
plt.xlabel('电影名')
plt.ylabel('人民币 (万)')

# 显示图例
plt.legend()

plt.grid()

# 展示图片
plt.show()
