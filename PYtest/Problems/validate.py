import re

def validate_employee(emp_id, email):
    # Validate Employee ID (EMP-1234)
    if not re.match(r"^EMP-\d{4}$", emp_id):
        raise ValueError("Invalid employee ID")

    # Validate Email (name@company.com)
    if not re.match(r"^[a-zA-Z0-9._%+-]+@company\.com$", email):
        raise ValueError("Invalid email")

    return True