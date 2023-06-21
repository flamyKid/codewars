# https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    answer = ''
    
    for i in str(num):
        answer += str(int(i) ** 2)
        
    return int(answer)
