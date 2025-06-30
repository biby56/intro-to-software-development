
def find_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("List of numbers is empty")
    return sum(numbers) / len(numbers)


def gardners_equation(velocity: float, alpha: float = 0.31, beta: float = 0.25) -> float:
    return alpha*velocity**beta
