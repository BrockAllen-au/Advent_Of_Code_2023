"""
Day 04: Scratch cards. Match winning numbers to numbers you have in each card.
Winning numbers are left of the '|' seperator. Your numbers are right of the '|' seperator.
"""
import re

INPUT_FILE = 'input_file_1.txt'
SEPARATORS = r'[:|]'


def main():
    total = 0

    with open(INPUT_FILE) as in_file:
        lines = [line.strip() for line in in_file]

    for line in lines:
        cards = re.split(SEPARATORS, line)
        # # Strip leading and trailing whitespace from each seperated list
        cards = [re.sub(r'^\s+|\s+$', '', part) for part in cards]
        winning_numbers = cards[1]
        winning_numbers = winning_numbers.split(" ")
        # Splitting with a space causes single numbers to have a 'space', causing lists to have blank
        # ' ' values in the list. Remove any blanks from the lists to ensure correct matching
        # Using just 'list.remove(''), only removes the first instance, so need to loop through lists
        for number in winning_numbers:
            if number == '':
                winning_numbers.remove('')
        your_numbers = cards[2]
        your_numbers = your_numbers.split(" ")
        for number in your_numbers:
            if number == '':
                your_numbers.remove('')
        matches = 0
        for number in winning_numbers:
            if number in your_numbers:
                matches += 1
        winning_score = 0
        if matches > 0:
            for i in range(matches):
                # First match gets 1 point
                if i == 0:
                    winning_score += 1
                # All other matches doubles the score
                else:
                    winning_score *= 2
        total += winning_score

    print(f"Part 01 total: {total}")


if __name__ == '__main__':
    main()
