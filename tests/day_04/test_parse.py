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

def test_update_item_type():
    grid = create_grid_from_input_list(simple_input)
    item = next(i for i in grid.items if i.x == 2 and i.y == 2)  # item at (2, 2)
    assert item.type == "."
    grid.update_item_type(item, "@")
    assert item.type == "@"
    grid.get_obstacles()
    assert item.accessible == True
    assert grid.count_accessible_items() == 5


def test_remove_accessible_items():
    grid = create_grid_from_input_list(simple_input)
    grid.get_obstacles()
    initial_accessible_count = grid.count_accessible_items()
    removed_count = grid.remove_accessible_items()
    assert removed_count == initial_accessible_count
    # After removal, count accessible items again
    grid.get_obstacles()
    new_accessible_count = grid.count_accessible_items()
    assert new_accessible_count == 0

def test_remove_accessible_items_complex():
    grid = create_grid_from_input_list(complex_input)
    grid.get_obstacles()
    initial_accessible_count = grid.count_accessible_items()
    removed_count = grid.remove_accessible_items()
    assert removed_count == initial_accessible_count
    assert initial_accessible_count == 11
    # After removal, count accessible items again
    grid.get_obstacles()
    new_accessible_count = grid.count_accessible_items()
    assert new_accessible_count == 1
    # One more removal:
    removed_2_count = grid.remove_accessible_items()
    grid.get_obstacles()
    assert removed_2_count == new_accessible_count
    final_accessible_count = grid.count_accessible_items()
    assert final_accessible_count == 1
