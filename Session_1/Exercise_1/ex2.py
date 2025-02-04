def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    first, second = 0, 1
    for _ in range(2, n):
        fib = first + second
        first, second = second, fib
    return fib

print(fibonacci(10)) 
print(fibonacci(4))
