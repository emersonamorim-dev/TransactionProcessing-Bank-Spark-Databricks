from datetime import datetime, timedelta

def format_date(date: datetime, format_str: str = "%Y-%m-%d") -> str:
    """Format a date."""
    return date.strftime(format_str)

def parse_date(date_str: str, format_str: str = "%Y-%m-%d") -> datetime:
    """Convert a string to a datetime object."""
    return datetime.strptime(date_str, format_str)

def date_difference(date1: datetime, date2: datetime) -> int:
    """Calculate the difference in days between two dates."""
    return (date2 - date1).days

def add_days(date: datetime, days: int) -> datetime:
    """Add a specific number of days to a date."""
    return date + timedelta(days=days)

def subtract_days(date: datetime, days: int) -> datetime:
    """Subtract a specific number of days from a date."""
    return date - timedelta(days=days)

def first_day_of_month(date: datetime) -> datetime:
    """Get the first day of the month for a specific date."""
    return datetime(date.year, date.month, 1)

def last_day_of_month(date: datetime) -> datetime:
    """Get the last day of the month for a specific date."""
    next_month = date.replace(day=28) + timedelta(days=4)  # this will never fail
    return next_month - timedelta(days=next_month.day)

def current_date() -> datetime:
    """Get the current date."""
    return datetime.now()

