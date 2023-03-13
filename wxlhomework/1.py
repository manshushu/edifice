import pandas as pd
w=pd.read_csv("EMSI_JobChange_UK.csv",encoding="gbk")
df=pd.DataFrame(w)
# print(df.loc['173':'192',["Jobs 2011","Jobs 2014"]])
# 第一问第二问
df.insert(1,'Change',value=df['Jobs 2014']-df['Jobs 2011'])
df.insert(1,'dChange',value=df['Change']/df['Jobs 2011'])
# print(df)
# 第三问
df.drop(columns=['Country'])
# 4
#5
print(df.loc['P',['City','Jobs 2011','Jobs 2014','Change']])
#6
print(df['Jobs 2011'].mean())
print(df['Jobs 2011'].max())
print(df['Jobs 2011'].min())
print(df['Jobs 2014'].mean())
print(df['Jobs 2014'].max())
#7
print(df['Jobs 2014'].mad())
print(df['Jobs 2011'].mad())
#根据平均值计算平均绝对利差