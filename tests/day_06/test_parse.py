from day_06.parse import Parser, Problem
import os
import pytest

test_input = """
3  5   4  8 10
94 18 48 20 39
+  *  *  +   +
"""
def test_parse_file_to_problems(tmp_path):
    test_file = tmp_path / "test_input.txt"
    test_file.write_text(test_input)
    parser = Parser()
    parser.parse_file_to_problems(str(test_file))
    
    assert len(parser.problems) == 5
    
    problem0 = parser.get_or_create_problem(0)
    assert problem0.numbers == [3, 94]
    assert problem0.operation == "+"
    assert problem0.solve() == 97  # 3 + 94
    
    problem1 = parser.get_or_create_problem(1)
    assert problem1.numbers == [5, 18]
    assert problem1.operation == "*"
    assert problem1.solve() == 90  # 5 * 18
    
    problem2 = parser.get_or_create_problem(2)
    assert problem2.numbers == [4, 48]
    assert problem2.operation == "*"
    assert problem2.solve() == 192  # 4 * 48
    
    problem3 = parser.get_or_create_problem(3)
    assert problem3.numbers == [8, 20]
    assert problem3.operation == "+"
    assert problem3.solve() == 28  # 8 + 20
    
    problem4 = parser.get_or_create_problem(4)
    assert problem4.numbers == [10, 39]
    assert problem4.operation == "+"
    assert problem4.solve() == 49  # 10 + 39

    parser.solve_all_problems()
    assert parser.problem_total == 97 + 90 + 192 + 28 + 49  # Total of all problem solutions
