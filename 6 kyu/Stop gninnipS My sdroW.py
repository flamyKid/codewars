# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    words = sentence.split()
    final_sentence = ''
    
    for word in words:
        if len(word) >= 5:
            final_sentence += word[::-1] + ' '
        else:
            final_sentence += word + ' '
            
    
    return final_sentence[0:-1]  # строка без пробела в конце
