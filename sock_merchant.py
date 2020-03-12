def sockMerchant(n, ar):
    # keep track of pairs you've found already
    socks = {}
    pairs = 0

    # loop through array
    for sock in ar:
        # if sock is already in dictionary: increment
        if sock in socks:
            socks[sock] += 1
        # else: add to dictionary with value 1
        else:
            socks[sock] = 1

    # loop through dictionary
    for sock in socks:
        value = socks[sock]
        # if value > 2
        if (value >= 2):
            # divide value by two
            num_pairs = value // 2 
            # increment pairs by value // 2
            pairs += num_pairs
            # decrement value by (value // 2) * 2
            # value -= num_pairs * 2
    return pairs 

li = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]
print(sockMerchant(20, li))