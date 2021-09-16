# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

def persistence(n):
    n = str(n)
    count = 0
    
    while len(n) != 1:
        multiply = 1
        
        nums = list(map(int, n))
        for num in nums:
            multiply *= num
        
        n = str(multiply)
        count += 1
        
    return count
