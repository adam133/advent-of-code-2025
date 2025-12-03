from parse import parse_file_to_str, parse_string_to_ranges, identify_invalid_ids_in_range, sum_nums
from typing import List


def main():
    ranges_str = parse_file_to_str('src/day_02/data/input.txt')
    ranges = parse_string_to_ranges(ranges_str)
    print(f"Parsed: {len(ranges)} ranges found.")
    invalid_ids_all: List[int] = []
    for range_check in ranges:
        invalid_ids_all.append(identify_invalid_ids_in_range(range_check))
    print(f"Identified {len(invalid_ids_all)} invalid IDs in ranges.")
    summed_invalid_ids = sum_nums([num for sublist in invalid_ids_all for num in sublist])
    print(f"Sum of all invalid IDs: {summed_invalid_ids}")

if __name__ == "__main__":
    main()
