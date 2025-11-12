#!/usr/bin/env python3

def print_fibonacci(length):
    list_to_store_values = list()
    for n in range(length):
        if len(list_to_store_values) == length:
            print(n)
            p = n + 1
            sum = p + n 
            print(p)
    pass

print_fibonacci(9)    
