def repeatedString(s, n):
    # get length of str
    l = len(s)
    # find the number of a's in the original string
    # and multiply them by the optimal number to
    # get the len(s) to be very close to the value of n
    # then add in the remainder count of a
    return (s.count('a') * (n//l) + s[:n%l].count('a'))

print(repeatedString('fdsjalfkdsafdsabfdsfdsjsadsabvasdhfdjkd', 1200000000))