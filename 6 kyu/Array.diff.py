# https://www.codewars.com/kata/523f5d21c841566fde000009

def array_diff(a, b):
    final_list = []
    
    for i in a:
        if i not in b:
            final_list.append(i)
            
    return final_list
