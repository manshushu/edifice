import pandas as pd

# 创建示例数据框
df = pd.DataFrame({'Name': ['Alice', 'Bob', 'Charlie'],
                   'ID': [1, 2, 3],
                   'Value': [10, 20, 30]})

# 创建空的第四列
df['NewValue'] = None

# 设置要匹配的值
match_value = 'Alice'

# 将第三列（Value）与第一列（Name）进行匹配，并在第四列（NewValue）中输出匹配到的结果
df.loc[df['Name'] == match_value, 'NewValue'] = df.loc[df['Name'] == match_value, 'Value']

# 打印修改后的数据框
print(df)