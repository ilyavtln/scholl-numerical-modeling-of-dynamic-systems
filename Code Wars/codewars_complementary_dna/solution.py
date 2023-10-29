def DNA_strand(dna):
    s = ""
    for i in dna:
        if i == "A":
            s += "T"
        elif i == "T":
            s += "A"
        elif i == "G":
            s += "C"
        elif i == "C":
            s += "G"
    return s