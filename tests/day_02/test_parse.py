from day_02.parse import parse_string_to_ranges, identify_invalid_ids_in_range, Range


def test_parse_string_to_ranges():
    input_string = "10-15,20-25"
    ranges = parse_string_to_ranges(input_string)
    assert len(ranges) == 2
    assert ranges[0].start == 10
    assert ranges[0].end == 15
    assert ranges[1].start == 20
    assert ranges[1].end == 25

def test_identify_invalid_ids_in_range():
    range = Range(10, 100)
    invalid_ids = identify_invalid_ids_in_range(range)
    expected_invalid_ids = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    assert invalid_ids == expected_invalid_ids

def test_identify_invalid_ids_in_small_range():
    range = Range(1, 20)
    invalid_ids = identify_invalid_ids_in_range(range)
    expected_invalid_ids = [11]
    assert invalid_ids == expected_invalid_ids

def test_identify_invalid_ids_in_no_invalid_range():
    range = Range(1, 9)
    invalid_ids = identify_invalid_ids_in_range(range)
    expected_invalid_ids = []
    assert invalid_ids == expected_invalid_ids

def test_identify_invalid_ids_in_larger_range():
    range = Range(100, 200)
    invalid_ids = identify_invalid_ids_in_range(range)
    expected_invalid_ids = []
    assert invalid_ids == expected_invalid_ids

def test_identify_invalid_ids_in_4_digit_range():
    range = Range(1000, 2000)
    invalid_ids = identify_invalid_ids_in_range(range)
    expected_invalid_ids = [1010, 1111, 1212, 1313, 1414, 1515, 1616, 1717, 1818, 1919]
    assert invalid_ids == expected_invalid_ids
