# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    answer = ''
    
    for word in sentence.split():
        if len(word) >= 5:
            answer += word[::-1] + ' '
        else:
            answer += word + ' '
            
    return answer[:-1]
