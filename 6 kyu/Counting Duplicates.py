# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

def duplicate_count(string):
    chars = []
    duplicates = []
    
    for char in string:
        char = char.lower()
        
        if char in chars:
            if char not in duplicates:
                duplicates.append(char)
        else:
            chars.append(char)
            
    return len(duplicates)
