
import pandas as pd
import re

# 读取Excel文件
df = pd.read_excel('1.xlsx')

# 创建新列
df['new_column'] = ''

# 遍历每一行，提取数字字符并写入新列
for index, row in df.iterrows():
    # 用正则表达式提取数字字符
    digits = ''.join(re.findall(r'\d', str(row['num'])))
    # 将提取出的数字字符写入新列
    df.at[index, 'new_column'] = digits

# 将DataFrame写入新的Excel文件，并保存
df.to_excel('new_file.xlsx', sheet_name='Sheet1', index=False)
