import numpy as np 
 
a = np.arange(25)  
print(a+'\n')
print (a.ndim)             # a 现只有一个维度
# 现在调整其大小
b = a.reshape(*list(range(3)))  # b 现在拥有三个维度
print (b)