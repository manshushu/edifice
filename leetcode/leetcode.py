class solution:
    def fib(self,n:int):
        a,b=1,1
        for _ in range(n):
            a,b=b,(a+b)%1000000007
        return a
    

    def numWays(self,n:int)->int:
        a,b=1,1
        for _ in range(n):
            a,b=b,(a+b)%1000000007
        return 
    

def isMatch(s: str, p: str) -> bool:
    # 定义 dp 数组，dp[i][j] 表示 s 的前 i 个字符是否能被 p 的前 j 个字符所匹配
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    # 初始化状态
    dp[0][0] = True
    # 处理 * 号匹配 0 次的情况
    for j in range(2, len(p) + 1):
        dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
    # 匹配过程
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] in {s[i - 1], '.'}:
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and p[j - 2] in {s[i - 1], '.'})
    # 返回结果
    return dp[-1][-1]


