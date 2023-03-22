import matplotlib.pyplot as plt
import numpy as np
import time
# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 输入统计数据
wendu = [250,300,325,350,375]
yichun1 = [34.05,
37.43,
46.94,
49.7,
47.21

]
yichun2 = [18.07,
17.28,
19.6,
30.62,
39.1


]
#谁和谁对比
a='A1'
b='A2'
bar_width = 0.3  # 条形宽度
index_male = np.arange(len(wendu))  # 男生条形图的横坐标
index_female = index_male + bar_width  # 女生条形图的横坐标

# 使用两次 bar 函数画出两组条形图
plt.bar(index_male, height=yichun1, width=bar_width, color='b', label=a)
plt.bar(index_female, height=yichun2, width=bar_width, color='g', label=b)

plt.legend()  # 显示图例
plt.xticks(index_male + bar_width/2, wendu)  # 让横坐标轴刻度显示 wendu 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.xlabel('温度')
plt.ylabel('C4烯烃选择性数值')  # 纵坐标轴标题
plt.title(a+'与'+b+'对照')  # 图形标题
# plt.savefig(time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) )
plt.show()