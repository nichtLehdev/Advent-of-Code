import os
import re

## Part 1
with open(os.path.dirname(__file__) + "/inputs/day1.txt", "r") as file:
    data = file.read().splitlines()
    sum = 0

    for row in data:

        # find all digits via RegEx and turn the first 
        # and last digit into one bigger digit
        digits = re.findall('\d', row)
        row_digit = digits[0] + digits[-1]
        sum += int(row_digit)

    print("Day 1, Part 1 --- Result: " + str(sum))


## Part 2
with open(os.path.dirname(__file__) + "/inputs/day1.txt", "r") as file:
    data = file.read().splitlines()
    sum = 0

    for row in data:

        # replaces each spelled digit with the digits and 
        # the adjacent chars that could be used by a different digit
        row = row.replace('one','o1e')
        row = row.replace('two','t2')
        row = row.replace('three','t3e')
        row = row.replace('four','4')
        row = row.replace('five','5e')
        row = row.replace('six','6')
        row = row.replace('seven','7n')
        row = row.replace('eight','e8t')
        row = row.replace('nine','n9e')

        # repeat part 1
        digits = re.findall('\d', row)
        row_digit = digits[0] + digits[-1]
        sum += int(row_digit)

    print("Day 1, Part 2 --- Result: " + str(sum))
