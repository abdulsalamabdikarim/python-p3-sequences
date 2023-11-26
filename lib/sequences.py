#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_numbers = list(0,)
    fibonacci_numbers.append(1)
    next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    for n in range(0, length):
        # n = fibonacci_numbers[len(fibonacci_numbers)-2] + fibonacci_numbers[len(fibonacci_numbers)-1]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers

print(print_fibonacci(10))
