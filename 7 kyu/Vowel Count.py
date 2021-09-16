# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count_vowel = 0
    
    for symbol in sentence:
        if symbol in vowels:
            count_vowel += 1
            
    return count_vowel
