import re
from common.utils import read_file
from typing import List
import numpy as np




def p2(input: List[str]) -> int:
    regex_game = re.compile(r"Game \d+") # matches "Game 1"
    regex_colors = re.compile(r"\d+ \w+") # matches "4 blue"

    games = {}
    for line in input:
        game_num = regex_game.search(line).group().split(" ")[1]
        games[game_num] = []

        subgames = line.split(";")

        for subgame in subgames:
            subgame = subgame.strip()
            games[game_num].append({})
            colors = regex_colors.findall(subgame)
            for color in colors:
                color = color.split(" ")
                games[game_num][-1][color[1]] = int(color[0])

    powers = 0
    for game in games:
        max_red = 0
        max_green = 0
        max_blue = 0
        for subgame in games[game]:
            max_red = max(max_red, subgame.get("red", 0))
            max_green = max(max_green, subgame.get("green", 0))
            max_blue = max(max_blue, subgame.get("blue", 0))
        powers += max_red * max_green * max_blue

    return powers

def p1(input: List[str]) -> int:
    red_cubes = 12
    green_cubes = 13
    blue_cubes = 14

    regex_game = re.compile(r"Game \d+") # matches "Game 1"
    regex_colors = re.compile(r"\d+ \w+") # matches "4 blue"

    games = {}
    for line in input:
        game_num = regex_game.search(line).group().split(" ")[1]
        games[game_num] = []

        subgames = line.split(";")

        for subgame in subgames:
            subgame = subgame.strip()
            games[game_num].append({})
            colors = regex_colors.findall(subgame)
            for color in colors:
                color = color.split(" ")
                games[game_num][-1][color[1]] = int(color[0])

    game_sum = 0
    for game in games:
        valid_game = True
        for subgame in games[game]:
            if subgame.get("red", 0) > red_cubes or subgame.get("green", 0) > green_cubes or subgame.get("blue", 0) > blue_cubes:
                valid_game = False
                break
        if valid_game:
            game_sum += int(game)

    return game_sum


if __name__ == "__main__":
    input = read_file("02/input.txt")
    # print(p1(input))
    print(p2(input))


# Game 1: 4 blue, 16 green, 2 red; 5 red, 11 blue, 16 green; 9 green, 11 blue; 10 blue, 6 green, 4 red