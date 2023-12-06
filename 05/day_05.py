from typing import List
from common.utils import read_file

def p1(input: List[str]) -> int:
    # Extract seeds
    seeds = list(map(int, input.pop(0).split(':')[1].split()))

    # Initialize dictionaries to store map values
    maps = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }

    current_map = None

    # Iterate through lines and parse map values
    for line in input:
        if line.startswith("seed-to-soil"):
            current_map = "seed-to-soil"
        elif line.startswith("soil-to-fertilizer"):
            current_map = "soil-to-fertilizer"
        elif line.startswith("fertilizer-to-water"):
            current_map = "fertilizer-to-water"
        elif line.startswith("water-to-light"):
            current_map = "water-to-light"
        elif line.startswith("light-to-temperature"):
            current_map = "light-to-temperature"
        elif line.startswith("temperature-to-humidity"):
            current_map = "temperature-to-humidity"
        elif line.startswith("humidity-to-location"):
            current_map = "humidity-to-location"
        elif line.strip() == "":
            current_map = None  # End of a map section
        else:
            destination, source, length = [int(x) for x in line.split()]
            # if (50, 98, 2) for example, then we want to store 50 -> 98 and 51 -> 99 ranges
            maps[current_map].append((range(source, source + length), range(destination, destination + length)))

    for i, seed in enumerate(seeds):
        # Find the map that contains the seed
        for _map in maps.values():
            # for source, destination in maps[map]:
            seed = p1_project_map(seed, _map)
        seeds[i] = seed
                
    
    return min(seeds)


def p1_project_map(number: int, _map: List[tuple]) -> int:
    for source_range, destination_range in _map:
        if number in source_range:
            return destination_range[number - source_range[0]]
    return number


def p2(input: List[str]) -> int:
    seeds = list(map(int, input.pop(0).split(':')[1].split()))
    seeds = [range(seed, seed + length) for seed, length in zip(seeds[::2], seeds[1::2])]


    # Initialize dictionaries to store map values
    maps = {
        "seed-to-soil": [],
        "soil-to-fertilizer": [],
        "fertilizer-to-water": [],
        "water-to-light": [],
        "light-to-temperature": [],
        "temperature-to-humidity": [],
        "humidity-to-location": [],
    }

    current_map = None

    # Iterate through lines and parse map values
    for line in input:
        if line.startswith("seed-to-soil"):
            current_map = "seed-to-soil"
        elif line.startswith("soil-to-fertilizer"):
            current_map = "soil-to-fertilizer"
        elif line.startswith("fertilizer-to-water"):
            current_map = "fertilizer-to-water"
        elif line.startswith("water-to-light"):
            current_map = "water-to-light"
        elif line.startswith("light-to-temperature"):
            current_map = "light-to-temperature"
        elif line.startswith("temperature-to-humidity"):
            current_map = "temperature-to-humidity"
        elif line.startswith("humidity-to-location"):
            current_map = "humidity-to-location"
        elif line.strip() == "":
            current_map = None  # End of a map section
        else:
            destination, source, length = [int(x) for x in line.split()]
            # if (50, 98, 2) for example, then we want to store 50 -> 98 and 51 -> 99 ranges
            maps[current_map].append((range(source, source + length), range(destination, destination + length)))

    for i, seed in enumerate(seeds):
        # Find the map that contains the seed
        for _map in maps.values():
            # for source, destination in maps[map]:
            seed = p2_project_map(seed, _map)
        seeds[i] = seed
                
    
    return min(seeds, key=lambda x: x.start)


def p2_project_map(_range: range, _map: List[tuple]) -> range:
    for source_range, destination_range in _map:
        intersection = range(max(source_range.start, _range.start), min(source_range.stop, _range.stop) + 1)
        if len(intersection) > 0:
            return range(intersection.start + destination_range.start - source_range.start, intersection.stop + destination_range.start - source_range.start)
    return _range

if __name__ == "__main__":
    input_data = read_file("05/input.txt")
    # print(p1(input_data))
    print(p2(input_data))
