import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cs_content = pd.read_csv(
    "citeseer\\citeseer.content", sep="\t", header=None, low_memory=False
)
cs_cite = pd.read_csv(
    "citeseer\\citeseer.cites", sep="\t", header=None, low_memory=False
)
content = np.array(cs_content)
df_cite = np.array(cs_cite)
x=input()
Sum=0
list=[]
num={}
for i in content:
    if (x==i[0]):   print(i[-1])
for i in df_cite:
    if (x==i[0]): list.append(i[1])
for i in content:
    for x in list:
        if(x==i[0]): num[x]=sum(i[1:-1])

# print(num)

plt.bar([i for i in num.keys()][:5], [i for i in num.values()][:5])

plt.xlabel('ID')
plt.ylabel('NUM')
plt.show()

