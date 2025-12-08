from day_06.parse import Parser, Problem
import os
import pytest

test_input = """
3  5   4  8 103
94 18 48 20 39 
1  1   1  1  1 
0   2 1  2  1  
+  *  *  +  +  
"""
def test_parse_file_to_problems(tmp_path):
    test_file = tmp_path / "test_input.txt"
    test_file.write_text(test_input)
    parser = Parser()
    parser.parse_file_to_problems(str(test_file))
    
    assert len(parser.problems) == 5
    assert parser.problems[0].start_char_id == 0
    assert parser.problems[0].end_char_id == 2
    assert parser.problems[0].operation == "+"
    assert parser.problems[0].numbers == [3910, 4]
    assert parser.problems[0].solve() == 4 + 3910

    assert parser.problems[1].operation == "*"
    assert parser.problems[1].numbers == [511, 82]
    assert parser.problems[1].solve() == 511 * 82

    assert parser.problems[-1].operation == "+"
    assert parser.problems[-1].start_char_id == 12
    assert parser.problems[-1].end_char_id == 14
    assert parser.problems[-1].numbers == [131, 91, 3]
    assert parser.problems[-1].solve() == 131 + 91 + 3
    
    parser.solve_all_problems()
    assert parser.problem_total == 66585
