import plotly.express as px

from die import Die

die = Die()

# 掷几次骰子把结果存在列表
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果，存储每个点数出现的次数
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 结果可视化
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()