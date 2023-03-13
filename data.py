data = '''250	0.4 	0.31
275	0.6 	0.42
300	1.1 	0.74
325	3.3 	1.16
350	6.0 	1.81
400	21.1 	3.79
250	0.5 	0.1
275	1.1 	0.32
300	3.0 	0.31
325	6.1 	0.69
350	9.6 	0.76
400	33.5 	2.68
250	2.1 	0.18
275	3.8 	0.35
300	5.8 	0.47
325	9.8 	0.77
350	15.9 	1.57
400	45.0 	3.93
250	2.8 	0.23
275	7.5 	0.15
300	12.6 	0.5
325	15.9 	1.04
350	27.0 	0.99
400	63.2 	4.11
250	4.4	0.13
275	7.9	0.15
300	11.7	0.2
325	17.8	1.42
350	30.2	1.53
400	69.4	2.51
'''
n = 6

list1 = data.splitlines()
# print(list1)
wendu = []
y1input = []
y2input = []
for i in list1:
    i = i.split('\t')
    wendu.append(float(i[0]))
    y1input.append(float(i[1]))
    y2input.append(float(i[2]))

l = [i for i in wendu]
wendu = [l[i:i + n] for i in range(0, len(l), n)]  #将五个一分
l = [i for i in y1input]
y1input = [l[i:i + n] for i in range(0, len(l), n)]
l = [i for i in y2input]
y2input = [l[i:i + n] for i in range(0, len(l), n)]
print(wendu)