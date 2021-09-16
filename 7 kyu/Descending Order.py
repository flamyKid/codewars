# https://www.codewars.com/kata/5467e4d82edf8bbf40000155

def descending_order(num):
    nums = list(map(int, str(num)))
    nums.sort()
    
    final_num = ''
    for i in nums:
        final_num += str(i)
        
    return int(final_num[::-1])
