from parse import create_grid_from_input_list, parse_file_to_list_str
import os

def main():
    input_list = parse_file_to_list_str("src/day_04/data/input.txt")
    grid = create_grid_from_input_list(input_list)
    print(f"Grid dimensions: {grid.width} x {grid.height}")
    grid.get_obstacles()
    accessible_count = grid.count_accessible_items()
    # grid.print_accessible_grid()
    print(f"Part 1: Number of accessible items: {accessible_count}")
    total_removed_count = 0

    while True:
        grid.get_obstacles()
        removed_count = grid.remove_accessible_items()
        if removed_count == 0:
            break
        total_removed_count += removed_count
        print(f"Removed {removed_count} accessible items.")
    print(f"Total removed accessible items: {total_removed_count}")
    grid.print_accessible_grid()

if __name__ == "__main__":
    main()