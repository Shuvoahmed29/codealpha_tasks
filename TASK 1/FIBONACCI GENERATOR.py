def fibonacci_generator(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

terms = int(input("Enter the number of Fibonacci terms to generate: "))
result = fibonacci_generator(terms)
print("Fibonacci Series:")
print(*result)
