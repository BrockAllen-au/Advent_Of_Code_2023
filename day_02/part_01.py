import re

INPUT_FILE = 'input_file_1.txt'
SEPARATORS = r'[:;]'
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
RED_SEARCH = r'\bred\b'


def main():
    total = 0

    with open(INPUT_FILE) as in_file:
        lines = [line.strip() for line in in_file]

    for line in lines:
        game_line = re.split(SEPARATORS, line)
        # Strip leading and trailing whitespace from each game in the line
        game_line = [re.sub(r'^\s+|\s+$', '', part) for part in game_line]
        # Extract the game ID number as an int
        game_id = int(re.findall(r'(\d+)', game_line[0])[0])
        game_valid = True
        # Start at index 1 as index 0 is the game_id
        for game in game_line[1:]:
            red = 0
            green = 0
            blue = 0
            # Splits each colour draw
            colours_drawn = game.strip().split(',')
            for colour in colours_drawn:
                # Splits the number and colour
                individual_colour = colour.strip().split(' ')
                if individual_colour[1] == 'red':
                    red += int(individual_colour[0])
                elif individual_colour[1] == 'green':
                    green += int(individual_colour[0])
                elif individual_colour[1] == 'blue':
                    blue += int(individual_colour[0])
                if red > MAX_RED or green > MAX_GREEN or blue > MAX_BLUE:
                    game_valid = False
        if game_valid:
            total += game_id

    print(f"Game_ID Total: {total}")


if __name__ == '__main__':
    main()
