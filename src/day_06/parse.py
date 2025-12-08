import os
from typing import List


class Problem:
    def __init__(self, problem_id: int, start_char_id: int, end_char_id: int, operator: str):
        self.problem_id = problem_id
        self.numbers: List[int] = []
        self.operation: str = operator
        self.start_char_id: int = start_char_id
        self.end_char_id: int = end_char_id
    
    def add_number(self, number: int):
        self.numbers.append(number)

    def set_operation(self, operation: str):
        self.operation = operation

    def solve(self) -> int:
        if self.operation == "+":
            return sum(self.numbers)
        elif self.operation == "*":
            result = 1
            for num in self.numbers:
                result *= num
            return result
        else:
            raise ValueError(f"Unsupported operation: {self.operation}")


class Parser:
    def __init__(self):
        self.problems: List[Problem] = []
        self.problem_total: int = None

    def create_problem(self, problem_id: int, start_char_id: int, end_char_id: int, operator: str) -> Problem:
        new_problem = Problem(problem_id, start_char_id=start_char_id, end_char_id=end_char_id, operator=operator)
        self.problems.append(new_problem)
        return new_problem
    
    def get_problem_for_char_id(self, char_id: int) -> Problem:
        for problem in self.problems:
            if problem.start_char_id <= char_id <= problem.end_char_id:
                return problem
        raise ValueError(f"No problem found for char_id: {char_id}")

    def parse_file_to_problems(self, file_path: str) -> list[str]:
        # get absolute path from relative path
        file_path = os.path.abspath(file_path)
        with open(file_path, 'r') as file:
            input_list = file.read().strip().split('\n')
        
        # read line 5 first to build problems:
        line5 = input_list[4]
        last_char_id = 0
        last_operator = ""
        problem_id = 0
        for char_id, char in enumerate(line5):
            if char == ' ':
                continue

            # for first and last problem, we need to adjust start and end char ids
            if problem_id == 0:
                problem_id += 1
                last_operator = char
                continue
            self.create_problem(problem_id=problem_id, start_char_id=last_char_id, end_char_id=char_id-1, operator=last_operator)
            last_char_id = char_id
            problem_id += 1
            last_operator = char
        # create last problem
        self.create_problem(problem_id=problem_id, start_char_id=last_char_id, end_char_id=len(line5) + 1, operator=last_operator)

        # Pivot: iterate through each character position, then through all lines
        num_char_positions = len(input_list[0])
        for char_id in range(num_char_positions):
            number = ""
            for line in input_list[:-1]:  # all lines except last
                if char_id < len(line):
                    char = line[char_id]
                    if char == ' ':
                        continue
                    else:
                        number += char
            if number:
                number_int = int(number)
                problem = self.get_problem_for_char_id(char_id)
                problem.add_number(number_int)


    def solve_all_problems(self) -> List[int]:
        results = [problem.solve() for problem in self.problems]
        self.problem_total = sum(results)
        return results
