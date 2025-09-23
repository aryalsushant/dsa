def sum_of_digits(num):
    total = 0
    num = abs(num)
    while num > 0:
        total += num%10
        num//=10

    return total

# Test cases
print(sum_of_digits(123))    # Expected output: 6 (1 + 2 + 3)
print(sum_of_digits(9876))   # Expected output: 30 (9 + 8 + 7 + 6)
print(sum_of_digits(0))      # Expected output: 0
print(sum_of_digits(-456))   # Expected output: 15 (4 + 5 + 6)
        
