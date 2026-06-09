"""Tests for src/models.py"""

from src.models import Invoice, Customer


def test_invoice_total():
    """Invoice.total() should calculate subtotal + tax."""
    inv = Invoice(
        invoice_id="INV-001",
        customer_name="John Doe",
        subtotal=100.0,
        tax_rate="8.5"
    )
    assert inv.total() == 108.50


def test_invoice_summary():
    """Invoice.summary() should return a formatted string."""
    inv = Invoice(
        invoice_id="INV-002",
        customer_name="  jane smith  ",
        subtotal=200.0,
        tax_rate="10"
    )
    result = inv.summary()
    assert "INV-002" in result
    assert "Jane Smith" in result
    assert "$" in result


def test_customer_display_name():
    """Customer.display_name() should normalize the name."""
    c = Customer(customer_id="C-001", name="  bob jones  ", email="bob@test.com")
    assert c.display_name() == "Bob Jones"


def test_customer_display_name_none():
    """Customer with None name should not crash."""
    c = Customer(customer_id="C-002", name=None, email="anon@test.com")
    result = c.display_name()
    assert result == "" or result is None
