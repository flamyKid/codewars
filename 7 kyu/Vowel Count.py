# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    cout = 0
    
    for char in sentence:
        if char in "aeiou":
            cout += 1
    
    return cout
