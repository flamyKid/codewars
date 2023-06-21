# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039

def accum(s):
    answer = ''
    count = 0
    
    for char in s:
        answer += char.upper() + char.lower() * count + '-'
        count += 1

    return answer[:-1]
