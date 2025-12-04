from day_03.parse import BatteryBank, parse_input_list_to_battery_bank


def test_parse_input_list_to_battery_bank():
    input_list = ["352817649", "987654321"]
    battery_banks = parse_input_list_to_battery_bank(input_list)
    assert len(battery_banks) == 2
    assert isinstance(battery_banks[0], BatteryBank)
    assert isinstance(battery_banks[1], BatteryBank)
    assert len(battery_banks[0].batteries) == 9
    assert len(battery_banks[1].batteries) == 9

def test_parse_battery_bank():
    battery_str = "352817649"
    battery_bank = BatteryBank(battery_str)
    assert len(battery_bank.batteries) == 9
    assert battery_bank.batteries[0].joltage == 3
    assert battery_bank.batteries[0].position == 0
    assert battery_bank.batteries[4].joltage == 1
    assert battery_bank.batteries[4].position == 4
    assert battery_bank.batteries[8].joltage == 9
    assert battery_bank.batteries[8].position == 8

def test_get_max_capacity_batteries():
    battery_str = "352817649"
    battery_bank = BatteryBank(battery_str)
    battery_1, battery_2 = battery_bank.get_max_capacity_batteries()
    assert battery_1.joltage == 8
    assert battery_1.position == 3
    assert battery_2.joltage == 9
    assert battery_2.position == 8

def test_get_max_joltage():
    battery_str = "352817649"
    battery_bank = BatteryBank(battery_str)
    max_joltage = battery_bank.get_max_joltage()
    assert max_joltage == 89

def test_get_max_capacity_batteries_v2():
    battery_str = "987654321123443543"
    battery_bank = BatteryBank(battery_str)
    max_batteries = battery_bank.get_max_capacity_batteries_v2()
    assert max_batteries[0].joltage == 9
    assert max_batteries[0].position == 0
    assert len(max_batteries) == 12
    assert max_batteries[-1].joltage == 3
    assert max_batteries[-1].position == 17

def test_get_max_joltage_v2():
    battery_str = "987654321123443543"
    battery_bank = BatteryBank(battery_str)
    max_joltage = battery_bank.get_max_joltage_v2()
    assert max_joltage == 987654443543
