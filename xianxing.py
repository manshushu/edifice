#导入包
from scipy import optimize
import numpy as np
mass_1=1
rou=1
jiasudu=9.8
P=1
M=1

#确定c,A,b,Aeq,beq
b_xishu=mass_1*rou*jiasudu*P
c = np.array([2,3,-5])
A = np.array([[-2,5,-1],[1,3,1]])
b = np.array([-10,12])
Aeq = np.array([[1,1,1]])
beq = np.array([7])

#求解
res = optimize.linprog(c,A,b,Aeq,beq)
print(res)

