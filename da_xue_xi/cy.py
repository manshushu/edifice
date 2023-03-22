
import pandas as pd
files=['1.xlsx','2.xlsx','3.xlsx','4.xlsx']
# 读取 CSV 文件并选择第一列
for file in files:
    df = pd.read_excel(file)
    df['result'] = df['num'].str.replace('\d+', '')
    df.to_excel("name.xlsx")
# print(df['result'])
# # 打印第一列数据
# print(column_data)
