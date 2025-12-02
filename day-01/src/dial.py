class Dial:
    def __init__(self, positions: int, start_position: int = 50):
        self.positions = positions
        self.current_position = start_position
        self.times_stopped_at_zero = 0
        self.times_past_zero = 0
    
    def check_for_zero(self) -> bool:
        return self.current_position == 0
    
    def _turn_dial(self, ticks: int) -> int:
        # Get absolute value of ticks to handle large turns
        # If over 100 ticks, count how many times we pass zero
        passes = abs(ticks) // self.positions
        self.times_past_zero += passes

        if ticks < 0:
            remaining_ticks_to_move = ticks + (passes * self.positions)
        else:
            remaining_ticks_to_move = ticks - (passes * self.positions)
        print(f"Turning dial by {ticks} ticks from {self.current_position}, remaining {remaining_ticks_to_move}, times past zero: {self.times_past_zero}.")
        if remaining_ticks_to_move != 0:
            if (remaining_ticks_to_move + self.current_position) >= self.positions or (remaining_ticks_to_move + self.current_position) <= 0:
                self.times_past_zero += 1
                print(f"Passed zero during this turn. {remaining_ticks_to_move} ticks from position {self.current_position}.")
        self.current_position = (self.current_position + remaining_ticks_to_move) % self.positions

    def turn(self, direction: str, ticks: int):
        if direction == 'L':
            self._turn_dial(-ticks)
        elif direction == 'R':
            self._turn_dial(ticks)
        else:
            raise ValueError("Direction must be 'L' or 'R'")
        if self.check_for_zero():
            self.times_stopped_at_zero += 1
