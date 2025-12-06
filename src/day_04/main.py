from parse import create_grid_from_input_list, parse_file_to_list_str
import os

def main():
    input_list = parse_file_to_list_str("src/day_04/data/input.txt")
    grid = create_grid_from_input_list(input_list)
    print(f"Grid dimensions: {grid.width} x {grid.height}")
    grid.get_obstacles()
    accessible_count = grid.count_accessible_items()
    # grid.print_accessible_grid()
    print(f"Number of accessible items: {accessible_count}")

if __name__ == "__main__":
    main()