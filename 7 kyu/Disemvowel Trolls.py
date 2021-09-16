# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    final_string = ''
    
    for char in string:
        if char.lower() not in vowels:
            final_string += char
    
    return final_string
