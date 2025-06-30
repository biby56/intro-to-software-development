
def find_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("List of numbers is empty")
    return sum(numbers) / len(numbers)
