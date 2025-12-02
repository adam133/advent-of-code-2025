from src.dial import Dial
from pytest import fixture

@fixture
def dial_fixture():
    return Dial(100, start_position=50)

def test_dial_initialization(dial_fixture):
    dial = dial_fixture
    assert dial.positions == 100
    assert dial.current_position == 50
    assert dial.times_stopped_at_zero == 0
    assert dial.times_past_zero == 0

def test_check_for_zero(dial_fixture):
    dial = dial_fixture
    assert not dial.check_for_zero()
    dial.current_position = 0
    assert dial.check_for_zero()

def test_turn_left(dial_fixture):
    dial = dial_fixture
    dial.turn('L', 10)
    assert dial.current_position == 40
    dial.turn('L', 50)
    assert dial.current_position == 90

def test_turn_right(dial_fixture):
    dial = dial_fixture
    dial.turn('R', 10)
    assert dial.current_position == 60
    dial.turn('R', 50)
    assert dial.current_position == 10

def test_turn_to_zero(dial_fixture):
    dial = dial_fixture
    dial.turn('L', 50)
    assert dial.current_position == 0
    assert dial.times_stopped_at_zero == 1
    assert dial.times_past_zero == 1
    dial.turn('R', 100)
    assert dial.current_position == 0
    assert dial.times_stopped_at_zero == 2
    assert dial.times_past_zero == 2

def test_turn_over_100_ticks(dial_fixture):
    dial = dial_fixture
    dial.turn('R', 150)
    assert dial.current_position == 0
    assert dial.times_stopped_at_zero == 1
    assert dial.times_past_zero == 2
    dial.turn('L', 250)
    assert dial.current_position == 50
    assert dial.times_stopped_at_zero == 1
    assert dial.times_past_zero == 4

def test_more_turns(dial_fixture):
    dial = dial_fixture
    dial.turn('R', 60)
    assert dial.current_position == 10
    assert dial.times_past_zero == 1
    dial.turn('L', 20)
    assert dial.current_position == 90
    assert dial.times_past_zero == 2
    dial.turn('R', 15)
    assert dial.current_position == 5
    assert dial.times_past_zero == 3
    dial.turn('L', 10)
    assert dial.current_position == 95
    assert dial.times_past_zero == 4
    dial.turn('R', 1050)
    assert dial.current_position == 45
    assert dial.times_past_zero == 13
