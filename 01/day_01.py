import re
from common.utils import read_file


def p1(input: list[str]) -> int:
    digits = []
    for i in input:
        integers = [int(x) for x in i if x.isdigit()]
        digits.append(int(f'{integers[0]}{integers[-1]}'))

    return sum(digits)


words_to_values = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def p2(input: list[str]) -> int:
    digits = []
    for line in input:
        integers = [(int(x), i) for i, x in enumerate(line) if x.isdigit()]
        # find all matches with words to values:
        for word, value in words_to_values.items():
            # Regex to check the word is in the line
            match = re.finditer(word, line)
            integers.extend([(value, m.start()) for m in match])

        # Sort the list by the index
        integers.sort(key=lambda x: x[1])

        # Unwrap list
        integers = [x[0] for x in integers]

        digits.append(int(f'{integers[0]}{integers[-1]}'))

    return sum(digits)


if __name__ == "__main__":
    input = read_file("01/input.txt")
    print(p1(input))
    print(p2(input))
