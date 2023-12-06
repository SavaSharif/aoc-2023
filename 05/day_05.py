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
            for seed in seeds:
                if seed in seed_to_soil:
                    seed_to_soil[seed] = destination + (seed - source)

        seeds = seed_to_soil.values()

    # from the last dict, get the lowest value 
    return min(seeds)

def p2(input: List[str]) -> int:
    seeds = [(int(x), int(y)) for x, y in input[0].split(" ")[1:]] # test input: 79 14 55 13
    # we want a list of 79-92 (length 14), 55-68 (length 13
    seeds = [seed - (len(seeds) - i) for i, seed in enumerate(seeds)]

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
            for seed in seeds:
                if seed in seed_to_soil:
                    seed_to_soil[seed] = destination + (seed - source)

        seeds = seed_to_soil.values()

    # from the last dict, get the lowest value 
    return min(seeds)

if __name__ == "__main__":
    input_data = read_file("05/input.txt")
    print(p1(input_data))
    print(p2(input_data))
