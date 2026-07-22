import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

# 散点图 c类似于参数color，但用于将一系列值关联到颜色映射。这里将参数c设置成了一个y坐标值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])
ax.ticklabel_format(style='plain')

plt.show()