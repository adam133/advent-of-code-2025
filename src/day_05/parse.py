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

    def is_item_valid(self, item_id: int) -> bool:
        for start, end in self.id_ranges:
            if start <= item_id <= end:
                return True
        return False

    def clean_ranges(self):
        self.id_ranges.sort()
        cleaned_ranges = []
        current_start, current_end = self.id_ranges[0]
        for start, end in self.id_ranges[1:]:
            # Check for overlap or adjacency
            if start <= current_end + 1:
                current_end = max(current_end, end)
            else:
                # No overlap, add the current range and start a new one
                cleaned_ranges.append((current_start, current_end))
                current_start, current_end = start, end
        cleaned_ranges.append((current_start, current_end))
        self.id_ranges = cleaned_ranges
    
    def count_valid_items(self) -> int:
        valid_count = 0
        for range_start, range_end in self.id_ranges:
            valid_count += (range_end - range_start + 1)
        return valid_count
