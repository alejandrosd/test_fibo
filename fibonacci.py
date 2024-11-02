def fibonacci_series(limite):
    fib_sequence = []
    a, b = 0, 1
    while a <= limite:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

fibonacci_sequence = fibonacci_series(21)
print(fibonacci_sequence)
