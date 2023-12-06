from typing import List
from common.utils import read_file

def p1(input: List[str]) -> int:

    durations = [int(x) for x in input[0].split()[1:]]
    record_distances = [int(x) for x in input[1].split()[1:]]

    races = list(zip(durations, record_distances))

    # solve how many seconds we need to charge, to get to the record distance
    total_options = 1
    for time, distance in races:
        num_options = 0

        for charging_time in range(0, time +1):
            speed = charging_time
            time_left = time - charging_time
            
            distance_traveled = speed * time_left
            if distance_traveled > distance:
                num_options += 1

        total_options *= num_options
    

    
    print(total_options)

    # one millimeter per millisecond


def p2(input: List[str]) -> int:
    duration = int(''.join([(x) for x in input[0].split()[1:]]))
    record_distance = int(''.join([(x) for x in input[1].split()[1:]]))

    total_options = 0
    for charging_time in range(0, duration +1):
        speed = charging_time
        time_left = duration - charging_time
        
        distance_traveled = speed * time_left
        if distance_traveled > record_distance:
            total_options += 1

    print(total_options)


if __name__ == "__main__":
    input_data = read_file("06/input.txt")
    print(p1(input_data))
    print(p2(input_data))
