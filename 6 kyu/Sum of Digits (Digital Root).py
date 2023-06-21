# https://www.codewars.com/kata/541c8630095125aba6000c00

def digital_root(n):
    digital_root = n  # если len(n) = 1
    
    while len(str(n)) != 1:
        digital_root = sum(list(map(int, str(n))))
        n = str(digital_root)

    return digital_root
