# https://www.codewars.com/kata/5467e4d82edf8bbf40000155

def descending_order(num):
    num_list = list(map(int, str(num)))
    num_list.sort()
    
    answer = ''
    for i in num_list:
        answer += str(i)
        
    return int(answer[::-1])
