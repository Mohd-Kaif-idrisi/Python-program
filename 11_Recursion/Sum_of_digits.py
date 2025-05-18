def sum_digit(n):
    if n == 0 or n == 1:
        return n
    else:
        return n + sum_digit(n-1)
    
print(sum_digit(5))    