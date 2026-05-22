import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 使用内置样式
plt.style.use('seaborn-v0_8')

# 可在一个图形(figure)中绘制一或多个绘图(plot)。变量fig表示由生成的一系列绘图构成的整个图形。变量ax标识图形中的绘图
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 图标题、label设置
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14)

# 打开matplotlib查看器并显示绘图
plt.show()