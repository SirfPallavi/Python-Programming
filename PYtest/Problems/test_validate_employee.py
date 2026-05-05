import pytest
from Problems.validate import validate_employee


# ✅ Test 1: Valid input
def test_validate_employee_valid():
    assert validate_employee("EMP-1234", "john@company.com") == True


# ❌ Test 2: Invalid Employee ID
def test_invalid_employee_id():
    with pytest.raises(ValueError, match="Invalid employee ID"):
        validate_employee("EMP-12", "john@company.com")


# ❌ Test 3: Invalid Email
def test_invalid_email():
    with pytest.raises(ValueError, match="Invalid email"):
        validate_employee("EMP-1234", "john@gmail.com")