from itertools import product
import re
from typing import List
from common.utils import read_file


def p1(input_data: List[str]):
    factor = 1
    groups = []
    for line in input_data:
        sequence, numbers = line.split(" ")
        numbers = list(map(int, numbers.split(",")))
        # repeat the sequence 5 times with ? as separator
        sequence = "?".join([sequence] * factor)
        # same for numbers but with , as separator
        numbers = (numbers) * factor
        groups.append((list(sequence), numbers))

    pattern = re.compile(r'#+')

    valid_count = 0

    for sequence, numbers in groups:
        question_marks = sequence.count("?")
        combinations = list(list(tup) for tup in product(['#', '.'], repeat=question_marks))
        counts = 0
        for combination in combinations:
            new_sequence = [combination.pop(0) if char == "?" else char for char in sequence]

            matches = pattern.findall("".join(new_sequence))
            matches = ["".join(match) for match in matches]

            lengths = [len(match) for match in matches]
            if lengths == numbers:
                counts += 1
        valid_count += counts

    return valid_count


if __name__ == "__main__":
    input_data = read_file("12/input.txt")
    result = p1(input_data)
    print(result)


