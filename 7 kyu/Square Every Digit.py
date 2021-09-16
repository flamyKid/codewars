# https://www.codewars.com/kata/546e2562b03326a88e000020

def square_digits(num):
    answer = ''
    
    for n in str(num):
        answer += str(int(n) ** 2)
        
    return int(answer)
