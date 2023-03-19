import numpy as np

a=np.array([[1,2],[4,4]])

print(a)

# import numpy as np 
# a = np.array([1,  2,  3], dtype = complex)  
# print (a)
import numpy as np 
 
a = np.arange(25)  
print(a+'\n')
print (a.ndim)             # a 现只有一个维度
# 现在调整其大小
b = a.reshape(*list(range(3)))  # b 现在拥有三个维度
print (b)