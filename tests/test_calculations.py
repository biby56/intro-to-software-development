from geo_calculator.calculations import find_average


def test_length_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6



def test_find_average() -> None:
    numbers = [2, 4, 6, 8, 10]
    expected_average = 6.0
    assert find_average(numbers) == expected_average
