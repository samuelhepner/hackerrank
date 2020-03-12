#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


cnt = Counter()


if __name__ == '__main__':
    s = input("What is your company name ~> ")
    if (len(s) > 3 and len(s) <= 10**4):
        for letter in list(s.lower()):
            cnt[letter] += 1

        for letter in cnt:
            print(letter + ' ' + str(cnt[letter]))
    else:
        print("You fool.")
    