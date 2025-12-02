from dial import Dial
from parse import parse_file_to_turns

def main():
    turns = parse_file_to_turns('day-01/data/input.txt')
    dial = Dial(100, start_position=50)
    for direction, ticks in turns:
        dial.turn(direction, ticks)

    print(f"Final Position: {dial.current_position}")
    print(f"Times ended at Zero: {dial.times_at_zero}")


if __name__ == "__main__":
    main()
