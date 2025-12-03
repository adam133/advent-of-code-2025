# from day_02.parse import parse_string_to_ranges, identify_invalid_ids_in_range, Range


# def test_parse_string_to_ranges():
#     input_string = "10-15,20-25"
#     ranges = parse_string_to_ranges(input_string)
#     assert len(ranges) == 2
#     assert ranges[0].start == 10
#     assert ranges[0].end == 15
#     assert ranges[1].start == 20
#     assert ranges[1].end == 25

# def test_identify_invalid_ids_in_range():
#     range = Range(10, 100)
#     invalid_ids = identify_invalid_ids_in_range(range)
#     expected_invalid_ids = [11, 22, 33, 44, 55, 66, 77, 88, 99]
#     assert invalid_ids == expected_invalid_ids
