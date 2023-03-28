import pandas as pd

# read xlsx s and create dataframes
df1 = pd.read_excel("1.xlsx", header=1)
df2 = pd.read_excel("2.xlsx", header=1)
df3 = pd.read_excel("3.xlsx", header=1)
df4 = pd.read_excel("4.xlsx", header=1)
# remove digits from 'Name' column of each dataframe
df1['name'] = df1['学号/卡号/工号'].str.replace('\d+', '')
df2['name'] = df2['学号/卡号/工号'].str.replace('\d+', '')
df3['name'] = df3['学号/卡号/工号'].str.replace('\d+', '')
df4['name'] = df4['学号/卡号/工号'].str.replace('\d+', '')

# drop the original 'Name' column
df1.drop(columns=['学号/卡号/工号'], inplace=True)
df2.drop(columns=['学号/卡号/工号'], inplace=True)
df3.drop(columns=['学号/卡号/工号'], inplace=True)
df4.drop(columns=['学号/卡号/工号'], inplace=True)
# merge all dataframes into a single dataframe
merged_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# write merged dataframe to excel 
merged_df.to_excel("name.xlsx", sheet_name='Sheet1', index=False)
