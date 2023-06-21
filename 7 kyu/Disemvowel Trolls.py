# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string):
    answer = ''
    
    for char in string:
        if char.lower() not in "aeiou":
            answer += char
            
    return answer
