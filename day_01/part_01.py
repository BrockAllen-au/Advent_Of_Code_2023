"""
Part One. Loop through each line and find the first number in the string for the first number,
then find the last number in the string as the second number. Combine the 2 numbers to create 1 number.
Then total all numbers together to get answer.
EG:
String: pqr3st5u8vwx
first_no = 3 ; second_no = 8 ; number for this string = 38
"""

INPUT_FILE = "input_01.txt"


def main():
    numbers = []

    with open(INPUT_FILE) as in_file:
        lines = []
        for line in in_file:
            lines.append(line.strip())

        for line in lines:
            rev_line = reversed(line)
            # Get first number in line
            for character in line:
                try:
                    # Once come to a number, stop
                    number = int(character)
                    number_01 = number
                    break
                except ValueError:
                    continue

            # Get first number in reversed line
            for character in rev_line:
                try:
                    # Once come to a number, stop
                    number = int(character)
                    number_02 = number
                    break
                except ValueError:
                    continue

            # Convert numbers to string to apply string concatenation
            n1 = str(number_01)
            n2 = str(number_02)
            n_final = n1 + n2
            # Append concatenated number to list as integer
            numbers.append(int(n_final))

    # Show the total of all numbers added together
    print(sum(numbers))


if __name__ == "__main__":
    main()
