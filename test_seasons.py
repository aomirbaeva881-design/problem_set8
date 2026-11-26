from datetime import date
from seasons import calculate_minutes


def test_calculate_minutes():
    assert calculate_minutes(date(2025, 1, 1), date(2025, 1, 2)) == 1440
    assert calculate_minutes(date(2025, 1, 1), date(2025, 1, 1)) == 0
    assert calculate_minutes(date(2024, 2, 28), date(2024, 3, 1)) == 2880