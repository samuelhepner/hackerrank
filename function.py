def is_leap(year):
    leap = False
    if (year >= 1900 and year <=10**5):
        if (year % 4 == 0):
            leap = True
            if (year % 100 == 0):
                leap = False
                if (year % 400 == 0):
                    leap = True


    return leap

year = int(input("Choose a year: "))
print(is_leap(year))