from itertools import product
from multiprocessing import Pool, cpu_count
import re
from typing import List
from common.utils import read_file
import time

pattern = re.compile(r'#+')

def p1(input_data: List[str]):
    start = time.time()
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

    end = time.time()
    print(end - start)
    return valid_count

def generate_combinations(sequence, numbers, index=0):
    if index == len(sequence):
        matches = pattern.findall("".join(sequence))
        matches = ["".join(match) for match in matches]
        lengths = [len(match) for match in matches]
        if lengths == numbers:
            yield sequence.copy()
        return

    if sequence[index] == "?":
        for char in ['#', '.']:
            sequence[index] = char
            yield from generate_combinations(sequence, numbers, index + 1)
            sequence[index] = "?"  # backtrack
    else:
        yield from generate_combinations(sequence, numbers, index + 1)


def p2_helper(args):
    sequence, numbers = args
    return len(list(generate_combinations(sequence, numbers)))

def p2(input_data: List[str]):
    start = time.time()
    factor = 2
    groups = []
    for line in input_data:
        sequence, numbers = line.split(" ")
        numbers = list(map(int, numbers.split(",")))
        sequence = list("?".join([sequence] * factor))
        numbers = (numbers) * factor
        groups.append((sequence, numbers))

    # Use multiprocessing
    with Pool(cpu_count()) as pool:
        counts = pool.map(p2_helper, groups)

    end = time.time()
    print(end - start)
    return sum(counts)


if __name__ == "__main__":
    input_data = read_file("12/input.txt")

    # result = p1(input_data)
    # print(result)
    result = p2(input_data)
    print(result)


