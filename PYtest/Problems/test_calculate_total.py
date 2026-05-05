import pytest
from Problems.calculate import calculate_total


def test_calculate_total_valid():
    assert calculate_total([100, 200, 300], 0.1) == 660



def test_calculate_total_negative_price():
    with pytest.raises(ValueError, match="Price cannot be negative"):
        calculate_total([100, -50, 200], 0.1)



def test_calculate_total_invalid_tax():
    with pytest.raises(ValueError, match="Invalid tax rate"):
        calculate_total([100, 200], 1.5)
