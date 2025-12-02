from src.parse import parse_file_to_turns, parse_list_to_turns, parse_input_as_list
from pytest import fixture


def sample_data():
    return ["L10", "R20", "L30", "R1051"]

def test_parse_input_as_list(tmp_path):
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("\n".join(sample_data()))

    result = parse_input_as_list(str(test_file))
    assert result == ["L10", "R20", "L30", "R1051"]

def test_parse_list_to_turns():
    input_array = ["L10", "R20", "L30", "R1051"]
    result = parse_list_to_turns(input_array)
    assert result == [('L', 10), ('R', 20), ('L', 30), ('R', 1051)]

def test_parse_file_to_turns(tmp_path):
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("\n".join(sample_data()))
    result = parse_file_to_turns(str(test_file))
    assert result == [('L', 10), ('R', 20), ('L', 30), ('R', 1051)]