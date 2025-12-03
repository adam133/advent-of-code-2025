class Dial:
    def __init__(self, positions: int, start_position: int = 50):
        self.positions = positions
        self.current_position = start_position
        self.times_stopped_at_zero = 0
        self.times_past_zero = 0
    
    def check_for_zero(self) -> bool:
        return self.current_position == 0
    
    def _check_position(self):
        # Wrap around the dial if necessary
        if self.current_position < 0:
            # negative wrap to positions - 1
            self.current_position = self.positions - 1
        elif self.current_position >= self.positions:
            # positive wrap to 0
            self.current_position = 0
            self.times_past_zero += 1
        elif self.current_position == 0:
            # Increment the count of times passed zero
            self.times_past_zero += 1

    def _turn_dial(self, ticks: int) -> int:
        while ticks != 0:
            if ticks > 0:
                self.current_position += 1
                ticks -= 1
            else:
                self.current_position -= 1
                ticks += 1
            self._check_position()

    def turn(self, direction: str, ticks: int):
        if direction == 'L':
            self._turn_dial(-ticks)
        elif direction == 'R':
            self._turn_dial(ticks)
        else:
            raise ValueError("Direction must be 'L' or 'R'")
        if self.check_for_zero():
            self.times_stopped_at_zero += 1
