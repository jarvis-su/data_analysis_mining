import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

plt.figure(figsize = (7, 5))
plt.show()

# 正弦余弦
x = np.linspace(0,2 * np.pi, 50)
y = np.sin(x)
plt.plot(x, y, 'bp--')
plt.show()

# 饼图
labels = 'Forgs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct='%1.1f%%', shadow = True, startangle = 90)
plt.axis
plt.show()

# 条形直方图
x = np.random.randn(1000)
plt.hist(x, 10)
plt.show()

# 箱线图
x = np.random.randn(1000)
D = pd.DataFrame([x, x + 1]).T
D.plot(kind = 'box')
plt.show()

# 对数
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
x = pd.Series(np.exp(np.arange(20)))
x.plot(label = u'原始数据图', legend = True)
plt.show()

x.plot(logy = True, label = u'对称数据图', legend = True)
plt.show()

# 误差条形图
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
error = np.random.randn(10)
y = pd.Series(np.sin(np.arange(10)))
y.plot(yerr = error)
plt.show()