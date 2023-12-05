import re
from typing import List
from common.utils import read_file

def p1(input: List[str]) -> int:
    seeds = [int(x) for x in input[0].split(" ")[1:]]
    # skip a line
    input = input[2:]

    # list of dicts
    conversions = []
    while input:
        line = input.pop(0)
        result = re.match(r"(\w+)-to-(\w+) map:", line)
        # if result is not None, then we have a new category
        if result:
            # append a new dict to conversions and fill it with the next 3 value tuples until we hit an empty line
            conversions.append({})
            while input:
                line = input.pop(0)
                if line == "":
                    break
                source, destination, length = line.split(" ")
                for i in range(int(length)):
                    conversions[-1][int(destination) + i] = int(source) + i

    seed_to_location = {}
    # look up for each seed where it ends up, if there is no 
    for seed in seeds:
        location = seed
        for conversion in conversions:
            location = conversion.get(location, location)
        seed_to_location[seed] = location
    # print the lowest value
    return min(seed_to_location.values())
    
        
    







if __name__ == "__main__":
    input_data = read_file("05/input.txt")
    print(p1(input_data))
    # print(p2(input_data))
