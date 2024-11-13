# generate_fibonacci.py

def generate_fibonacci_up_to(limit):
    fibonacci_sequence = []
    a, b = 0, 1
    while a <= limit:
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

# Generar la secuencia de Fibonacci hasta 21
fibonacci_sequence = generate_fibonacci_up_to(21)

# Guardar la secuencia en un archivo llamado "fibonacci.txt"
with open("fibonacci.txt", "w") as file:
    file.write(", ".join(map(str, fibonacci_sequence)))

print("Fibonacci sequence up to 21 has been written to fibonacci.txt.")
