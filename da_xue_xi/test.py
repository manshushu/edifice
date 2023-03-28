import pandas as pd

# 生成示例数据
data = {'col1': ['A', 'B', 'C', 'A', 'A', 'B', 'C', 'C', 'D'],
        'col2': [1, 2, 3, 4, 5, 6, 7, 8, 9]}
df = pd.DataFrame(data)

# 使用 groupby() 方法计数，并将结果输出到新的一列
df['count'] = df.groupby(['col1']).transform('count')

# 保证第一列没有重复值
df = df.drop_duplicates(['col1'])

# 打印结果
print(df)
