class Solution:
    def robot(self, a, b,k):
        def dfs(m: 'int', n: 'int', k: 'int') -> int:
            if not 0 <= m < a or not 0 <= n < b or not m % 10+m/10+n % 10+n/10 <= k:
                return False
            if m == a-1 and n == b-1:
                return True
            result = dfs(m+1, n, k)+dfs(m, n-1, k) + \
                dfs(m-1, n, k)+dfs(m, n+1, k)
            return result

        for i in range(a):
            for j in range(b):
                dfs(i,j,k)
