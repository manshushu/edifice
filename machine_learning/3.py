import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.api import anova_lm
import matplotlib.pyplot as plt
import pandas as pd
from patsy import dmatrices
import itertools as it
import random



df = pd.read_csv('data.csv',encoding='gbk')



target = 'C4烯烃收率'
variate = set(df.columns)  


x = []
variate_add = []
variate_del = variate.copy()

y = random.sample(variate,3) #随机生成一个选模型，3为变量的个数

for i in y:
    variate_add.append(i)
    x.append(i)
    variate_del.remove(i)

global aic   
formula="{}~{}".format("y","+".join(variate_add))  
aic=smf.ols(formula=formula,data=df).fit().aic  
print("随机化选模型为：{}~{}，对应的AIC值为：{}".format("y","+".join(variate_add), aic))
print("\n")



#添加变量
def forwark():
    score_add = []
    global best_add_score
    global best_add_c
    print("添加变量")
    for c in variate_del:
        formula = "{}~{}".format("y", "+".join(variate_add+[c]))
        score = smf.ols(formula = formula, data = df).fit().aic
        score_add.append((score, c))   #将添加的变量，以及新的AIC值一起存储在数组中
        
        print('自变量为{}，对应的AIC值为：{}'.format("+".join(variate_add+[c]), score))

    score_add.sort(reverse=True)  #对数组内的数据进行排序，选择出AIC值最小的
    best_add_score, best_add_c = score_add.pop()
    
    print("最小AIC值为：{}".format(best_add_score))
    print("\n")

#删除变量
def back():
    score_del = []
    global best_del_score
    global best_del_c
    print("剔除变量")
    for i in x:

        select = x.copy() #copy一个集合，避免重复修改到原集合
        select.remove(i)
        formula = "{}~{}".format("y","+".join(select))
        score = smf.ols(formula = formula, data = df).fit().aic
        print('自变量为{}，对应的AIC值为：{}'.format("+".join(select), score))
        score_del.append((score, i))

    score_del.sort(reverse=True) #排序，方便将最小值输出
    best_del_score, best_del_c = score_del.pop()  #将最小的AIC值以及对应剔除的变量分别赋值
    print("最小AIC值为：{}".format(best_del_score))
    print("\n")

print("剩余变量为：{}".format(variate_del))
forwark()
back()

while variate:
      
#     forwark()
#     back()
    if(aic < best_add_score < best_del_score or aic < best_del_score < best_add_score):
        print("当前回归方程为最优回归方程，为{}~{}，AIC值为：{}".format("y","+".join(variate_add), aic))
        break
    elif(best_add_score < best_del_score < aic or best_add_score < aic < best_del_score):
        print("目前最小的aic值为{}".format(best_add_score))
        print('选择自变量：{}'.format("+".join(variate_add + [best_add_c])))   
        print('\n')
        variate_del.remove(best_add_c)
        variate_add.append(best_add_c)
        print("剩余变量为：{}".format(variate_del))
        aic = best_add_score
        forwark()
    else:
        print('当前最小AIC值为：{}'.format(best_del_score))
        print('需要剔除的变量为：{}'.format(best_del_c))
        aic = best_del_score   #将AIC值较小的选模型AIC值赋给aic再接着下一轮的对比
        x.remove(best_del_c)  #在原集合上剔除选模型所对应剔除的变量
        back()