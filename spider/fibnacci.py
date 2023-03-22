# class solution:
def fibnacci(n):
    if n==0: return 0
    if n==1: return 1
    return fibnacci(n-1)+fibnacci(n-2)
# classic recursion

def fibnacci_cut(n,dp):
    if n==0: return 0
    if n==1: return 1
    if dp[n]!=0: return dp[n]
    dp[n]=fibnacci_cut(n-1,dp)+fibnacci_cut(n-2,dp)
    return dp[n]
# (pruning) dp[n] print

def fib_memorized(n):
    dp=[0]*(n+1)
    return fibnacci_cut(n,dp)
# 开完数组直接调用

def testfib(n):
    # print(fibnacci(n))
    print(fib_memorized(n))
# for test

def dp_solve_fib(n):
    if n==0: return 0
    dp=[0]*(n+1)
    dp[0],dp[1]=0,1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]

    return dp[n]

# 写程序的时候一开始都是状态，定义环节，抽象成变量把他写出来
# 第二阶段就是吧最边界的情况返回值写出来
# 之后就是无尽的关键语句和循环判断，难得就多几个函数
def max_cake_price(n,price_list):
    if n<=1: return price_list[n]
    dp=[0]*(n+1)
    for j in range(1,n+1):
        for i in range(j):
            dp[j]=max(dp[j],dp[i]+price_list[j-i])
    return dp[j]

testfib(100)


