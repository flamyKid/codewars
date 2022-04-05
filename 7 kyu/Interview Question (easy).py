# https://www.codewars.com/kata/5b358a1e228d316283001892

def get_strings(city):
    count_char = {}
    
    for char in city.lower():
        if char in count_char:
            count_char[char] += '*'
        else:
            if char != ' ':  # чтобы не записывало пробелы
                count_char[char] = '*'
            
    # преобразование в одну строку
    answer = ''
    for char in count_char:
        answer += f'{char}:{count_char[char]},'
    
    return answer[0:-1]
