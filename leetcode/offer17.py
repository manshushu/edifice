from typing import List

class Solution:
    def printNumbers(self,n:int)-> List[int]:
        def dfs(x):
            if x == n:
                res.append(''.join(num))
                return
            for i in range(10):
                num[x] =str(i)
                dfs(x+1)

        num = ['0']* n
        res=[]
        dfs(0)
        return ',' .join(res)