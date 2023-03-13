def fibonacci(n):
    a, b = 0, 1
 
    for i in range(n):
        yield a
        a, b = b, a + b
 
fib = fibonacci(5)

print("Fibonacci sequence:")
for i in fib:
    print(i)
