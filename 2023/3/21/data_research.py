import pandas as pd
df=pd.read_csv("d:\\electricityConsumptionAndProductioction.csv")

field_data = df['Consumption']  # 提取所需的字段数据
time=df['DateTime']
# 主要是作图，搞点什么数据呢

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# plt.hist(time,field_data)  # 绘制10个条形区间的直方图
plt.xlabel('time')
plt.ylabel('amount')
plt.title('consumption')
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(12))
plt.show()
