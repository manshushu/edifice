nested_list = [1,2,3]

summ=[]
for i in nested_list:
    temp=nested_list.remove(i)
    summ.append(sum(i,temp))

print(summ)