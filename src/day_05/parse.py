import os
from typing import List


class Parser:
    def __init__(self):
        self.id_ranges: list[tuple[int, int]] = []
        self.items: List[int] = []

    def parse_file_to_db(self, file_path: str) -> list[str]:
        # get absolute path from relative path
        file_path = os.path.abspath(file_path)
        with open(file_path, 'r') as file:
            input_list = file.read().strip().split('\n')
        for line in input_list:
            if "-" in line:
                start, end = map(int, line.split("-"))
                self.id_ranges.append((start, end))
            elif line.isdigit():
                self.items.append(int(line))
