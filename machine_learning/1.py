import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import time
from scipy.sparse import data

i=0
deg = 3
wendu1 = [[250.0, 275.0, 300.0, 325.0, 350.0, 400.0], [250.0, 275.0, 300.0, 325.0, 350.0, 400.0], [250.0, 275.0, 300.0, 325.0, 350.0, 400.0], [250.0, 275.0, 300.0, 325.0, 350.0, 400.0], [250.0, 275.0, 300.0, 325.0, 350.0, 400.0]]
y1input1 =[[0.4, 0.6, 1.1, 3.3, 6.0, 21.1], [0.5, 1.1, 3.0, 6.1, 9.6, 33.5], [2.1, 3.8, 5.8, 9.8, 15.9, 45.0], [2.8, 7.5, 12.6, 15.9, 27.0, 63.2], [4.4, 7.9, 11.7, 17.8, 30.2, 69.4]]
y2input1 =  [[0.31, 0.42, 0.74, 1.16, 1.81, 3.79], [0.1, 0.32, 0.31, 0.69, 0.76, 2.68], [0.18, 0.35, 0.47, 0.77, 1.57, 3.93], [0.23, 0.15, 0.5, 1.04, 0.99, 4.11], [0.13, 0.15, 0.2, 1.42, 1.53, 2.51]]


while i<5:
    wendu = np.array(wendu1[0])
    y1original = np.array(y1input1[0])
    y2original = np.array(y2input1[0])
    z1 = np.polyfit(wendu, y1original, deg)  # 用3次多项式拟合  可以改为5 次多项式。。。。 返回三次多项式系数

    p1 = np.poly1d(z1)

    z2 = np.polyfit(wendu, y2original, deg)
    p2 = np.poly1d(z2)
    y1polyfit = p1(wendu)
    y2polyfit = p2(wendu)
    xnew = np.linspace(wendu.min(), wendu.max(), 300)
    func1 = interp1d(wendu, y1polyfit, kind='cubic')
    y1new = func1(xnew)
    func2 = interp1d(wendu, y2polyfit, kind='cubic')
    y2new = func2(xnew)
    plot1 = plt.plot(wendu, y1original, 'b', label='Ethanol conversion rate')
    plot2 = plt.plot(xnew, y1new, 'r', label='Ethanol conversion Curve Fitting')
    plot3 = plt.plot(wendu, y2original, 'g', label='Ethylene selectivity')
    plot4 = plt.plot(xnew, y2new, 'y', label='Ethylene selectivity Curve Fitting')
    plt.title("B"+str(i+3))
    plt.legend(loc=1)
    plt.savefig(time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) )
    plt.clf()
    i=i+1
    wendu1.pop(0)
    y1input1.pop(0)
    y2input1.pop(0)
    time.sleep(1)
# plt.show()
