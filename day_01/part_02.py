"""
Part Two. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six,
seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""

import re

INPUT_FILE = "input_01.txt"
NUMBER_DICT = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}


def main():
    total = 0

    with open(INPUT_FILE) as in_file:
        lines = []
        for line in in_file:
            lines.append(line.strip())

        for line in lines:
            # Iterate through and find all numbers in the string
            line_numbers = extract_numbers(line)
            if len(line_numbers) == 1:
                if line_numbers[0] in NUMBER_DICT.keys():
                    number = int(NUMBER_DICT.get(line_numbers[0]) + NUMBER_DICT.get(line_numbers[0]))
                else:
                    number = int(line_numbers[0] + line_numbers[0])
            else:
                # Get the first and last number from the list as required
                # This then only performs searches/conversions on 2 elements rather than the whole list
                first_last_numbers = [line_numbers[0], line_numbers[-1]]
                converted_numbers = []
                for item in first_last_numbers:
                    if item in NUMBER_DICT.keys():
                        converted_numbers.append(NUMBER_DICT.get(item))
                    else:
                        converted_numbers.append(item)
                number = int(converted_numbers[0] + converted_numbers[-1])

            total += number

    print(total)


def extract_numbers(line):
    numbers = []
    # Expression uses ?= to perform a positive lookahead assertion to find overlapping matches
    # \d finds single numerical digits
    pattern = re.compile(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))')
    matches = pattern.findall(line)
    for match in matches:
        numbers.append(match)
    return numbers


if __name__ == "__main__":
    main()
