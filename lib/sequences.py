#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    if length > 0:
        fib_list.append(0)
    if length >= 2:
        fib_list.append(1)
        for i in range(2, length):
            fib_list.append(fib_list[-1] + fib_list[-2])
    print(fib_list)

