import re

class InputSanitizationError(Exception):
    pass


def sanitize_input(text):
    # Keep letters, numbers, spaces, hyphen
    cleaned = re.sub(r"[^a-zA-Z0-9\s-]", "", text)

    # Remove extra spaces
    cleaned = cleaned.strip()

    if cleaned == "":
        raise InputSanitizationError("Invalid input after sanitization")

    return cleaned