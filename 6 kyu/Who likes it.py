# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    lenght = len(names)
    
    if lenght == 0:
        return 'no one likes this'
    elif lenght == 1:
        return f'{names[0]} likes this'
    elif lenght == 2:
        return f'{names[0]} and {names[1]} like this'
    elif lenght == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {lenght - 2} others like this'
