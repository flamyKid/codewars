# https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a, b):
    final_list = []
    
    for elem in a:
        if elem not in b:
            final_list.append(elem)
            
    return final_list
