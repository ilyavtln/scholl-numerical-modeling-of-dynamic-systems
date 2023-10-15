def likes(names):
    le = len(names)
    if le == 0:
        return 'no one likes this'
    elif le == 1:
        return f'{names[0]} likes this'
    elif le == 2:
        return f'{names[0]} and {names[1]} like this'
    elif le == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {le - 2} others like this'
