# https://www.codewars.com/kata/54da5a58ea159efa38000836

def find_it(seq):
    cout_num = {}
    
    for num in seq:
        if num in cout_num:
            cout_num[num] += 1
        else:
            cout_num[num] = 1
            
    for num, cout in cout_num.items():
        if cout % 2 != 0:
            return num
