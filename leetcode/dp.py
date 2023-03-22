def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_plus(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]


def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 核心思想就是避免重复计算


def fibonacci_plus_plus(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    cache[n] = result
    return result



def test_main():
   
   a= fibonacci_plus_plus(10)
   print(a)      


test_main()