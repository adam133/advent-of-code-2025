from typing import List
from dataclasses import dataclass
import os


class Direction:
    LEFT = 'L'
    RIGHT = 'R'

@dataclass
class Turn:
    direction: Direction
    ticks: int


def parse_input_as_list(file_path: str) -> List[str]:
    input_array = []
    with open(file_path, 'r') as file:
        for line in file:
            input_array.append(line.strip())
    return input_array

def parse_list_to_turns(input_array: List[str]) -> List[Turn]:
    turns = []
    for line in input_array:
        direction = Direction.LEFT if line[0] == 'L' else Direction.RIGHT
        ticks = int(line[1:])
        turns.append((direction, ticks))
    return turns

def parse_file_to_turns(file_path: str) -> List[Turn]:
    # get absolute path from relative path
    file_path = os.path.abspath(file_path)
    input_array = parse_input_as_list(file_path)
    return parse_list_to_turns(input_array)
