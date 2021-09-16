# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    n = str(n)
    
    while len(n) != 1:
        num_sum = sum(list(map(int, n)))
        n = str(num_sum)
        
    return int(n)
