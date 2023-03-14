'''
首先理解题目意思
对于n个骰子，会有几种和？ 答案是 5n+1种

那么题目就可以翻译成
有n个骰子，然后计算每种和的概率，那么这个问题和骰子就毫无关系
n个集合，每个集合中是1-6，然后计算所有集合中任选一个加起来再成为一个新的和集合，和集合中的重复的数都归一，然后求每个不相同和的概率


'''

# 第一种暴力法


#sum_collection=[touzi_num*n]   #这样就不对了，这是做了笛卡尔积，我想要的就是复制n份
#print(sum_collection)
# 如果使用暴力是不是还得写递归？，写循环怎么能使三个列表相加？


result=[]


# 创建原始的列表
my_list = [1, 2, 3, 4, 5, 6]

# 复制 my_list n 次，这里设为 3
n = 3
new_lists = [my_list.copy() for _ in range(n)]  # 使用列表推导式快速复制列表
print(sum(new_lists))
# 将所有列表的元素合并到一个列表中，并进行去重
unique_sum = list(set(sum(new_lists, [])))

# 输出结果
print(unique_sum)
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum_list = [sum(x) for x in zip(*nested_list)]
print(sum_list)



my_list = [[1, 2], [3, 4], [5, 6]]
new_list = []

for i in range(len(my_list)):
    for j in range(i + 1,len(my_list)):
        temp_list = [sum(x) for x in zip(my_list[i], my_list[j])]
        new_list.append(temp_list)

print(new_list)

# 每次看到for都要看半天，for没啥好看的，主要是看他的参数啊，循环是为了什么呢，是遍历，是想保证整个事件的完成
# 嵌套循环呢，就无所谓了，外面的先搞好再关心内部。


# 搞一堆不定的东西很难实现，尽可能搞定的东西
import itertools
nested_list = [1,2,3]

summ=[]
for i in nested_list:
    temp=nested_list.remove(i)
    summ.append(sum(i,temp))

print(summ)