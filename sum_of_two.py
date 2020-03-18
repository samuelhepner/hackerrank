def sumOfTwo(a, b, v):
    a = set(a)
    for value_b in b:
        if ((v - value_b) in a):
            return True
    return False
