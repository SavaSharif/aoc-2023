from typing import List
from common.utils import read_file

def p1(input: List[str]) -> int:
    seeds = [int(x) for x in input[0].split(" ")[1:]]
    input = input[2:]

    while input:
        input = input[1:]
        # seeds = list(mappings.values()) if mappings else seeds # already initialize with the seeds
        seed_to_soil = {seed: seed for seed in seeds}
        
        while input:
            line = input.pop(0)
            if line == "":
                break

            destination, source, length = [int(x) for x in line.split(" ")]
            for i in range(length):
                if source + i in seeds:
                    seed_to_soil[source + i] = destination + i

        seeds = seed_to_soil.values()

    # from the last dict, get the lowest value
    lowest = min(seeds)
    print(lowest)


if __name__ == "__main__":
    input_data = read_file("05/input.txt")
    print(p1(input_data))
    # print(p2(input_data))
