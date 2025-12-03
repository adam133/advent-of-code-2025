from dataclasses import dataclass
import os


@dataclass
class Range:
    start: int
    end: int


def parse_string_to_ranges(input_string):
    ranges = input_string.strip().split(',')
    range_objects = []
    for r in ranges:
        start, end = map(int, r.split('-'))
        range_objects.append(Range(start, end))
    return range_objects

def identify_invalid_ids_in_range(range_check: Range) -> list[int]:
    nums_to_check = [n for n in range(range_check.start, range_check.end + 1)]
    invalid_ids = []
    for n in nums_to_check:
        # for each number, convert to string, split in half, 
        # check if first half matches second half
        n_str = str(n)
        n_str_len = len(n_str)
        first_half = n_str[:n_str_len // 2]
        for i in range(1, len(first_half) + 1):
            # check how many times the substring appears in the number
            if n_str.count(first_half) >= 2:
                invalid_ids.append(n)
                break
            else:
                # remove the last character from the first half and try again
                first_half = first_half[:-1]
    return invalid_ids

def sum_nums(num_list: list[int]) -> int:
    return sum(num_list)

def parse_file_to_str(file_path: str) -> str:
    # get absolute path from relative path
    file_path = os.path.abspath(file_path)
    with open(file_path, 'r') as file:
        input_string = file.read().strip()
    return input_string
