from parse import Parser, Problem
import os

def main():
    parser = Parser()
    parser.parse_file_to_problems('src/day_06/data/input.txt')
    parser.solve_all_problems()
    print(f"Total of all problem solutions: {parser.problem_total}")


if __name__ == "__main__":
    main()
