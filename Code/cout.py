c_del = lambda : 2

c_ins = lambda : 2

def c_sub(x, y):
    if x == y:
        return 0
    if x == "A" and y == "T" or x == "T" and y == "A":
        return 3
    if x == "C" and y == "G" or x == "G" and y == "C":
        return 3
    return 4
