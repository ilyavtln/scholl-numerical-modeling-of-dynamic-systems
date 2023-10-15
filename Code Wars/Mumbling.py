def accum(s):
    new_s = ''
    for i in range(0, len(s)):
        if i == 0:
            new_s += s[i].upper()
            continue
        new_s += '-' + s[i].upper() + s[i].lower() * i
    return new_s
