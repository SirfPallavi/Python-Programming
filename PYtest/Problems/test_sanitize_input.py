import pytest
from sanitize_input import sanitize_input, InputSanitizationError


# ✅ Valid input
def test_sanitize_valid():
    assert sanitize_input("John Doe!") == "John Doe"


# ❌ Only special characters
def test_sanitize_empty():
    with pytest.raises(InputSanitizationError, match="Invalid input after sanitization"):
        sanitize_input("!@#$%")


# ✅ Mixed input
def test_sanitize_mixed():
    assert sanitize_input("Payment: 100$") == "Payment 100"