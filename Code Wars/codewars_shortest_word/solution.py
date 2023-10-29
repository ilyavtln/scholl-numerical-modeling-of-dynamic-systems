def find_short(s):
    words = s.split()
    l = len(words[0])
    for i in words:
        if len(i) <= l:
            l = len(i)
    return l # l: shortest word length