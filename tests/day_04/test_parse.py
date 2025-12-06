from day_04.parse import Grid, Item, parse_file_to_list_str, create_grid_from_input_list
import os
import pytest

simple_input = [
        "...@..",
        ".@....",
        "......",
        "..@.@."
    ]
complex_input = [
        "...@..@@@@@.@",
        ".@....@@@@@@@",
        "......@@@@@.@",
        "..@.@.@@@@@.@"
    ]


def test_init_grid():
    grid = create_grid_from_input_list(simple_input)
    assert grid.width == 6
    assert grid.height == 4
    assert len(grid.items) == 24
    first_item = grid.items[0]
    assert first_item.x == 0
    assert first_item.y == 0
    assert first_item.type == "."
    second_to_last_item = grid.items[-2]
    assert second_to_last_item.x == 4
    assert second_to_last_item.y == 3
    assert second_to_last_item.type == "@"

def test_get_item_neighbors():
    grid = create_grid_from_input_list(simple_input)
    item = next(i for i in grid.items if i.x == 2 and i.y == 2)  # item at (2, 2)
    neighbors = grid.get_item_neighbors(item)
    neighbor_positions = [(n.x, n.y) for n in neighbors]
    expected_positions = [(1, 2), (3, 2), (2, 1), (2, 3), (1, 1), (3, 1), (1, 3), (3, 3)]
    assert set(neighbor_positions) == set(expected_positions)

def test_get_obstacles_and_count_accessible_items():
    grid = create_grid_from_input_list(simple_input)
    grid.get_obstacles()
    accessible_count = grid.count_accessible_items()
    # Manually count accessible items based on the obstacle rule
    assert accessible_count == 4

def test_get_obstacles_and_count_accessible_items_complex():
    grid = create_grid_from_input_list(complex_input)
    grid.get_obstacles()
    accessible_count = grid.count_accessible_items()
    # Manually count accessible items based on the obstacle rule
    grid.print_accessible_grid()
    assert accessible_count == 11
