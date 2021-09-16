# https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    count_num = {}
    
    for num in seq:
        if num in count_num:
            count_num[num] += 1
        else:
            count_num[num] = 1
    
    for key, value in count_num.items():
        if value % 2 != 0:
            return key
