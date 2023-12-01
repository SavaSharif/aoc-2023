import re
from common.utils import read_file
from typing import List
import numpy as np

def p1(input: List[str]) -> int:
    digits = [re.findall(r"\d", line) for line in input]
    numbers = [int("".join(digit[0] + digit[-1])) for digit in digits]

    return sum(numbers)


def p2(input: List[str]) -> int:
    # dictionary with the string representation of the digit as key and the digit as value
    bla = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six':'6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        '0': '0',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
    }

    regex = re.compile(r"(?=(zero|one|two|three|four|five|six|seven|eight|nine|\d))")
    digits = [regex.findall(line) for line in input]

    # turn strings into digits
    digits =  [[bla[digit] for digit in line] for line in digits]

    # join the first and last digit to a number
    numbers = [int("".join(digit[0] + digit[-1])) for digit in digits]

    return sum(numbers)

if __name__ == "__main__":
    input = read_file("01/input.txt")
    # print(p1(input))
    print(p2(input))
