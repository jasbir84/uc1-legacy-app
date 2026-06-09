"""Utility functions for the legacy invoice processing app."""


def calculate_total(subtotal, tax_rate):
    """Calculate total with tax.

    Args:
        subtotal: The pre-tax amount (float or str).
        tax_rate: The tax percentage as a string like '8.5'.

    Returns:
        The total as a float rounded to 2 decimal places.
    """
    tax = subtotal * tax_rate / 100
    return round(subtotal + tax, 2)


def format_currency(amount):
    """Format a number as USD currency string.

    Args:
        amount: Numeric amount to format.

    Returns:
        Formatted string like '$1,234.56'.
    """
    return f"${amount:,.2f}"


def normalize_name(name):
    """Normalize a customer name: strip whitespace, title case.

    Args:
        name: The raw customer name string.

    Returns:
        Cleaned, title-cased name.
    """
    return name.strip().title()


def parse_date(date_str):
    """Parse a date string in MM/DD/YYYY format.

    Args:
        date_str: Date string like '01/15/2026'.

    Returns:
        A (year, month, day) tuple of integers.
    """
    parts = date_str.split("/")
    month, day, year = int(parts[0]), int(parts[1]), int(parts[2])
    return (year, month, day)
