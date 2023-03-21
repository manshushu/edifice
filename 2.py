# -*- coding: utf-8 -*-
import pandas as pd
from numpy import *

gray = pd.read_excel("d:\\electricityConsumptionAndProductioction.xlsx")
gray = (gray - gray.min()) / (gray.max() - gray.min())
std = gray.iloc[:, 0]
ce = gray.iloc[:, 1:]
n = ce.shape[0]
m = ce.shape[1]

a = zeros([m, n])
for i in range(m):
    for j in range(n):
        a[i, j] = abs(ce.iloc[j, i]-std[j])

c = amax(a)
d = amin(a)

result = zeros([m, n])
for i in range(m):
    for j in range(n):
        result[i, j] = (d+0.5*c)/(a[i, j]+0.5*c)

result2 = zeros(m)
for i in range(m):
    result2[i] = mean(result[i, :])
RT = pd.DataFrame(result2)
RT.to_csv("D:/result2.csv")
