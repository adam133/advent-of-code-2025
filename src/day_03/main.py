from parse import parse_file_to_list_of_str, parse_input_list_to_battery_bank, BatteryBank


def main():
    input_list = parse_file_to_list_of_str('src/day_03/data/input.txt')
    battery_banks = parse_input_list_to_battery_bank(input_list)
    print(f"Parsed: {len(battery_banks)} battery banks found.")
    max_joltage = 0
    for bank in battery_banks:
        max_joltage += bank.get_max_joltage_v2()
    print(f"Total max joltage from all battery banks: {max_joltage}")

if __name__ == "__main__":
    main()
