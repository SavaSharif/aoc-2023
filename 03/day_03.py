import re
from typing import List
from common.utils import read_file

def p1(input: List[str]) -> int:
    
    grid = []
    symbols = []
    numbers = []
    for line in input:
        split = re.findall(r'\d+|[a-zA-Z\W]', line)
        i = 0
        while i < len(split):
            if split[i].isnumeric() and i >= 0 and split[i] != split[i - 1]:
                # Duplicate the numeric character for its length
                split[i:i] = [split[i]] * (len(split[i]) - 1)
                i += len(split[i]) - 1
            elif not split[i].isnumeric() and split[i] != ".":
                symbols.append((len(grid), i))
            i += 1
            
        grid.append(split)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].isnumeric():
                numbers.append((i, j))

    neighboured = []
    # check for each number if it is neighbored by a symbol
    for number in numbers:
        for symbol in symbols:
            if abs(number[0] - symbol[0]) <= 1 and abs(number[1] - symbol[1]) <= 1:
                print(number, symbol)
                neighboured.append((number, symbol))

    sum = 0
    for i, ((y, x), (ys, xs)) in enumerate(neighboured):
        (prev_y, prev_x), _ = neighboured[i - 1]
        if y != prev_y or x != prev_x + 1:
            sum += int(grid[y][x])
        
    return sum

def p2(input: List[str]) -> int:
    grid = []
    symbols = []
    numbers = []
    for line in input:
        split = re.findall(r'\d+|[a-zA-Z\W]', line)
        i = 0
        while i < len(split):
            if split[i].isnumeric() and i >= 0 and split[i] != split[i - 1]:
                # Duplicate the numeric character for its length
                split[i:i] = [split[i]] * (len(split[i]) - 1)
                i += len(split[i]) - 1
            elif not split[i].isnumeric() and split[i] == "*":
                symbols.append((len(grid), i))
            i += 1
            
        grid.append(split)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].isnumeric():
                numbers.append((i, j))

    neighboured = []
    # check for each number if it is neighbored by a symbol
    for number in numbers:
        for symbol in symbols:
            if abs(number[0] - symbol[0]) <= 1 and abs(number[1] - symbol[1]) <= 1:
                print(number, symbol)
                neighboured.append((number, symbol))

    bla = 0
    # sort on symbol position
    neighboured.sort(key=lambda x: x[1])
    for i, ((y, x), (ys, xs)) in enumerate(neighboured):
        (prev_y, prev_x), (prev_ys, prev_xs) = neighboured[i - 1]
        prev_number = int(grid[prev_y][prev_x])
        number = int(grid[y][x])
        if (ys == prev_ys and xs == prev_xs) and (y != prev_y or x != prev_x + 1):
            bla += prev_number * number
        
    return bla

if __name__ == "__main__":
    input_data = read_file("03/input.txt")
    # print(p1(input_data))
    print(p2(input_data))
