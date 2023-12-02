import os
import re

input = open(os.path.dirname(__file__) + "/inputs/day2.txt", "r")
input_lines = input.read().splitlines()

# Part 1
# Check for each game(line) if the game would be possible with 12 red, 13 green and 14 blue cubes
# This is the case if the max amount of cubes shown of each color in each set is lower than these numbers

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

sum = 0

for game in input_lines:
    id = int(re.findall('\d+', game.split(':')[0])[0])

    sets = game.split(':')[1].split(';')

    game_possible = True

    for set in sets:
        cube_groups = set.split(',')
        for group in cube_groups:
            amount = re.findall('\d+', group)[0]
            color = group.split(' ')[-1]

            if color.lower() == 'red':
                if int(amount) > MAX_RED:
                    game_possible = False
            elif color.lower() == 'green':
                if int(amount) > MAX_GREEN:
                    game_possible = False
            else:
                if int(amount) > MAX_BLUE:
                    game_possible = False
            
    if game_possible:
        sum += id


print ("Day 2, Part 1 --- Result: " + str(sum))

sum = 0

# Part 2

for game in input_lines:
    sets = game.split(':')[1].split(';')

    MIN_RED = 0
    MIN_GREEN = 0
    MIN_BLUE = 0

    power = 0

    for set in sets:
        cube_groups = set.split(',')
        for group in cube_groups:
            amount = re.findall('\d+', group)[0]
            color = group.split(' ')[-1]

            if color.lower() == 'red':
                if int(amount) > MIN_RED:
                    MIN_RED = int(amount)
            elif color.lower() == 'green':
                if int(amount) > MIN_GREEN:
                    MIN_GREEN = int(amount)
            else:
                if int(amount) > MIN_BLUE:
                    MIN_BLUE = int(amount)
        
    power = MIN_BLUE * MIN_GREEN * MIN_RED
    sum += power

print ("Day 2, Part 2 --- Result: " + str(sum))