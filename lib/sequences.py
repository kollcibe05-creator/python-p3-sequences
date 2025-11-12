#!/usr/bin/env python3


def print_fibonacci(length):
    if length <= 0:
        return []
    elif length == 1:
        return [1]
    else:
        fib_list = [0, 1] 
        while len(fib_list) < length:
            next_in_list = fib_list[-1] + fib_list[-2]
            fib_list.append(next_in_list)       
        return fib_list

print_fibonacci(9)    
