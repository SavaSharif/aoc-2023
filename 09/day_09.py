from typing import List
from common.utils import read_file


def p1(input: List[str]) -> int:
    histories = [[int(num) for num in line.split()] for line in input]
    summed = 0
    for history in histories:
        sequences = []
        sequences.append(history)
        sequence = history
        while not all([i == 0 for i in sequence]):
            sequence = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
            sequences.append(sequence)

        sequences.reverse()

        for i, sequence in enumerate(sequences[:-1]):
            if i == 0:
                sequence.append(0)

            current_last_num = sequence[-1]
            last_num = sequences[i+1][-1]

            total = last_num + current_last_num
            sequences[i+1].append(total)

        summed += sequences[-1][-1]

    return summed

def p2(input: List[str]) -> int:
    histories = [[int(num) for num in line.split()] for line in input]
    summed = 0
    for history in histories:
        sequences = []
        sequences.append(history)
        sequence = history
        while not all([i == 0 for i in sequence]):
            sequence = [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
            sequences.append(sequence)

        sequences.reverse()

        for i, sequence in enumerate(sequences[:-1]):
            if i == 0:
                # add 0 as the first number in the sequence
                sequence.insert(0, 0)

            current_first_num = sequence[0]
            first_num = sequences[i+1][0]
            total = first_num - current_first_num
            sequences[i+1].insert(0, total)

        summed += sequences[-1][0]

    return summed



if __name__ == "__main__":
    input_data = read_file("09/input.txt")
    # result = p1(input_data)
    result = p2(input_data)
    print(result)
