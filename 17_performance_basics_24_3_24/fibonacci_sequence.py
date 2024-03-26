def fibonacci_sequence(num_elements):
    sequence = []
    a, b = 0, 1
    for _ in range(num_elements):
        sequence.append(a)
        a, b = b, a + b
    return sequence

num_elements = 10
fib_sequence = fibonacci_sequence(num_elements)
print(fib_sequence)

num_elements = 100
fib_sequence = fibonacci_sequence(num_elements)
print(fib_sequence)

num_elements = 1000
fib_sequence = fibonacci_sequence(num_elements)
print(fib_sequence)


######################################

def fibonacci_sequence_recursive(num_elements, sequence=None):
    if sequence is None:
        sequence = [0, 1]
    next_number = sequence[-1] + sequence[-2] 
    sequence.append(next_number)

    return fibonacci_sequence_recursive(num_elements, sequence)

num_elements = 10
fib_sequence = fibonacci_sequence_recursive(num_elements)
print(fib_sequence)

num_elements = 100
fib_sequence = fibonacci_sequence_recursive(num_elements)
print(fib_sequence)


num_elements = 1000
fib_sequence = fibonacci_sequence_recursive(num_elements)
print(fib_sequence)