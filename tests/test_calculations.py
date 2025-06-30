import pytest
from geo_calculator.calculations import *


def test_length_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6



def test_find_average() -> None:
    numbers = [2, 4, 6, 8, 10]
    expected_average = 6.0
    assert find_average(numbers) == expected_average

def test_gardners_equation():
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)
