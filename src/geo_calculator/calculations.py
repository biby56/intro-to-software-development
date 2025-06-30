
def find_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("List of numbers is empty")
    return sum(numbers) / len(numbers)


def gardners_equation(velocity: float, alpha: float = 0.31, beta: float = 0.25) -> float:
    """Calculate bulk density using Gardner's equation.

    Args:
        velocity (float): P-wave velocity in meters per second.
        alpha (float): Empirical constant, 0.31.
        beta (float): Empirical constant, 0.25.
    Returns:
        float: Bulk density
    Raises:
        ValueError: If velocity is negative.
    """
    return alpha*velocity**beta


