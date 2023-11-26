#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_numbers = [0,1]
    for number in range(0, length):
        next_number = fibonacci_numbers[len(fibonacci_numbers)-2] + fibonacci_numbers[len(fibonacci_numbers)-1]
        fibonacci_numbers.append(next_number)
    return fibonacci_numbers

print(print_fibonacci(7))
