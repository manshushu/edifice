import pandas as pd

# 创建一个 DataFrame
data = {'name': ['Alice', 'Bob', 'Cathy', 'David', 'Alice'],
        'age': [25, 26, 27, 28, 25],
        'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Beijing']}
df = pd.DataFrame(data)

# 使用 duplicated 方法检查 DataFrame 中的重复行
duplicated = df.duplicated()

print(df)
