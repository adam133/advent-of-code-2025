import os


class Battery:
    def __init__(self, position: int, joltage: int):
        self.position: int = position
        self.joltage: int = joltage

class BatteryBank:
    def __init__(self, battery_list: str):
        self.battery_str: str = battery_list
        self.batteries: list[Battery] = self._parse_batteries()
    
    def _parse_batteries(self) -> list[Battery]:
        batteries = []
        position = 0
        battery_entries = [b for b in self.battery_str]
        for entry in battery_entries:
            battery = Battery(position, int(entry))
            batteries.append(battery)
            position += 1
        return batteries
    
    def get_max_capacity_batteries(self) -> tuple[Battery, Battery]:
        # max joltage is the combined joltage of two batteries
        # maximize joltage of the first position batter + joltage of the second position battery
        battery_1 = self.batteries[0]
        battery_2 = self.batteries[-1]
        # get max joltage first battery
        # can't be last battery in bank
        for b in self.batteries[1:-1]:
            if b.joltage > battery_1.joltage:
                battery_1 = b
        # get max joltage second battery, must be after first battery
        for b in self.batteries[:-1]:
            if b.joltage > battery_2.joltage and b.position > battery_1.position:
                battery_2 = b
        return (battery_1, battery_2)
    
    def get_max_joltage(self) -> int:
        battery_1, battery_2 = self.get_max_capacity_batteries()
        joltage_str = str(battery_1.joltage) + str(battery_2.joltage)
        return int(joltage_str)
    
    def get_max_capacity_batteries_v2(self) -> list[Battery]:
        # max joltage is the combined joltage of twelve batteries
        # maximize joltage of the first position battery + joltage of the second position battery
        n = len(self.batteries)
        k = min(12, n)
        stack: list[Battery] = []
        for i, b in enumerate(self.batteries):
            # number of items remaining after this one: n - i - 1
            # we can pop if doing so still allows filling k items
            while stack and stack[-1].joltage < b.joltage and (len(stack) - 1 + (n - i)) >= k:
                stack.pop()
            if len(stack) < k:
                stack.append(b)
        return stack[:k]
    
    def get_max_joltage_v2(self) -> int:
        max_batteries = self.get_max_capacity_batteries_v2()
        joltage_str = "".join([str(b.joltage) for b in max_batteries])
        return int(joltage_str)

def parse_file_to_list_of_str(file_path: str) -> list[str]:
    # get absolute path from relative path
    file_path = os.path.abspath(file_path)
    with open(file_path, 'r') as file:
        input_list = file.read().strip().split('\n')
    return input_list

def parse_input_list_to_battery_bank(input: list[str]) -> list[BatteryBank]:
    battery_banks = []
    for input_str in input:
        battery_banks.append(BatteryBank(input_str))
    return battery_banks
