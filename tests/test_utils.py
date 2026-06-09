"""Tests for src/utils.py"""

from src.utils import calculate_total, format_currency, normalize_name, parse_date


def test_calculate_total_basic():
    """Tax calculation with numeric tax rate."""
    result = calculate_total(100.0, "8.5")  # tax_rate comes as string from CSV
    assert result == 108.50


def test_calculate_total_zero_tax():
    """Zero tax should return the subtotal unchanged."""
    result = calculate_total(250.0, "0")
    assert result == 250.0


def test_format_currency():
    """Should format as USD with commas and 2 decimal places."""
    assert format_currency(1234.5) == "$1,234.50"
    assert format_currency(0) == "$0.00"


def test_normalize_name():
    """Should strip whitespace and title-case."""
    assert normalize_name("  john doe  ") == "John Doe"
    assert normalize_name("ALICE SMITH") == "Alice Smith"


def test_normalize_name_none():
    """Should handle None gracefully (common in CSV imports)."""
    result = normalize_name(None)
    assert result == "" or result is None  # Either is acceptable


def test_parse_date():
    """Should parse MM/DD/YYYY into (year, month, day) tuple."""
    assert parse_date("01/15/2026") == (2026, 1, 15)
    assert parse_date("12/31/2025") == (2025, 12, 31)
