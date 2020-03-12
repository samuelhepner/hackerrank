def jumpingOnClouds(c):
    # keep track of jumps
    jumps = 0
    # start with i = 0
    i = 0
    # loop while i < len(c)
    while i < len(c)-1:
        # if we're one place away from the end
        if (i == len(c)-2):
            i+=1
            jumps += 1
        # if c[i+1] == 1: i += 2 and jumps += 1
        elif (c[i+1] == 1):
            i += 2
            jumps += 1
        # elif c[i+2] == 0: i += 2 and jumps += 1
        elif (c[i+2] == 0):
            i += 2
            jumps += 1
        # elif  c[i+2] == 1: i += 1 and jumps += 1
        elif (c[i+2] == 1):
            i += 1
            jumps += 1
    return jumps