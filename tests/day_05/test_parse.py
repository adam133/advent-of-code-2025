from day_05.parse import Parser
import os
import pytest


test_input = """
1-3
5-7
10

3
15-20
8"""

def test_parse_file_to_db(tmp_path):

    test_file = tmp_path / "test_input.txt"
    test_file.write_text(test_input)
    parser = Parser()
    parser.parse_file_to_db(str(test_file))
    assert parser.id_ranges == [(1, 3), (5, 7), (15, 20)]
    assert parser.items == [10, 3, 8]

def test_is_item_valid():
    parser = Parser()
    parser.id_ranges = [(1, 3), (5, 7)]
    assert parser.is_item_valid(2) is True
    assert parser.is_item_valid(4) is False
    assert parser.is_item_valid(6) is True
    assert parser.is_item_valid(8) is False

def test_clean_ranges():
    parser = Parser()
    parser.id_ranges = [(1, 3), (2, 5), (10, 15), (14, 20), (25, 30), (30, 31)]
    parser.clean_ranges()
    assert parser.id_ranges == [(1, 5), (10, 20), (25, 31)]

def test_count_valid_items():
    parser = Parser()
    parser.id_ranges = [(1, 3), (5, 7), (10, 15)]
    assert parser.count_valid_items() == 3 + 3 + 6
