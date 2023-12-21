"""
Part Two no longer checks if the game was impossible or not.
Just check if dice number for the particular colour is greater than it's previous value for that game set.
Iterate through each game set, multiply red, green blue.
Add to list and sum the list to get final total.
"""
import re

INPUT_FILE = 'input_file_1.txt'
SEPARATORS = r'[:;]'


def main():
    dice_multiplied = []

    with open(INPUT_FILE) as in_file:
        lines = [line.strip() for line in in_file]

    for line in lines:
        game_line = re.split(SEPARATORS, line)
        # Strip leading and trailing whitespace from each game in the line
        game_line = [re.sub(r'^\s+|\s+$', '', part) for part in game_line]
        # Extract the game ID number as an int
        game_id = int(re.findall(r'(\d+)', game_line[0])[0])
        red = 0
        green = 0
        blue = 0
        # Start at index 1 as index 0 is the game_id
        for game in game_line[1:]:
            # Splits each colour draw
            colours_drawn = game.strip().split(',')
            for colour in colours_drawn:
                # Splits the number and colour
                individual_colour = colour.strip().split(' ')
                if individual_colour[1] == 'red':
                    if int(individual_colour[0]) > red:
                        red = int(individual_colour[0])
                elif individual_colour[1] == 'green':
                    if int(individual_colour[0]) > green:
                        green = int(individual_colour[0])
                elif individual_colour[1] == 'blue':
                    if int(individual_colour[0]) > blue:
                        blue = int(individual_colour[0])

        dice_multiplied.append(red * green * blue)

    total = sum(dice_multiplied)
    print(f"Part 02 total: {total}")


if __name__ == '__main__':
    main()
