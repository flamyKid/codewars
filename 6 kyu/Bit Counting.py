# https://www.codewars.com/kata/526571aae218b8ee490006f4

def count_bits(num):
    count_bits = 0
    
    for digit in str(bin(num)):
        if digit == '1':
            count_bits += 1
    
    return count_bits
