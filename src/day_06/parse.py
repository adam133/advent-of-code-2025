import os
from typing import List


class Problem:
    def __init__(self, problem_id: int):
        self.problem_id = problem_id
        self.numbers: List[int] = []
        self.operation: str = ""
    
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

    def get_or_create_problem(self, problem_id: int) -> Problem:
        for problem in self.problems:
            if problem.problem_id == problem_id:
                return problem
        new_problem = Problem(problem_id)
        self.problems.append(new_problem)
        return new_problem

    def parse_file_to_problems(self, file_path: str) -> list[str]:
        # get absolute path from relative path
        file_path = os.path.abspath(file_path)
        with open(file_path, 'r') as file:
            input_list = file.read().strip().split('\n')

        for line in input_list:
            problems = line.split(' ')
            problem_id = 0
            for problem in problems:
                if problem == '':
                    continue
                problem_obj = self.get_or_create_problem(problem_id)
                if str(problem) not in ('+', '*'):
                    problem_obj.add_number(int(problem))
                else:
                    problem_obj.set_operation(problem)
                problem_id += 1

    def solve_all_problems(self) -> List[int]:
        results = [problem.solve() for problem in self.problems]
        self.problem_total = sum(results)
        return results
