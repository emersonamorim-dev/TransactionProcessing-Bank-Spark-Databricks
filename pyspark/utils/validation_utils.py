import re
from datetime import datetime

def validate_email(email: str) -> bool:
    """Validate an email address."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))

def validate_phone_number(phone: str) -> bool:
    """Validate a phone number."""
    pattern = r"^\+?(\d[\d-. ]+)?(\([\d-. ]+\))?[\d-. ]+\d$"
    return bool(re.match(pattern, phone))

def validate_url(url: str) -> bool:
    """Validate a URL."""
    pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    return bool(re.match(pattern, url))

def validate_date(date_str: str, format_str: str = "%Y-%m-%d") -> bool:
    """Validate a date string."""
    try:
        datetime.strptime(date_str, format_str)
        return True
    except ValueError:
        return False

def validate_string_length(s: str, min_len: int = 0, max_len: int = None) -> bool:
    """Validate the length of a string."""
    if max_len is not None:
        return min_len <= len(s) <= max_len
    return min_len <= len(s)

def validate_numeric_range(value: float, min_val: float = None, max_val: float = None) -> bool:
    """Validate if a numeric value is within a specified range."""
    if min_val is not None and value < min_val:
        return False
    if max_val is not None and value > max_val:
        return False
    return True


