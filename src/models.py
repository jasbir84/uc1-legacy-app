"""Invoice model for the legacy app."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Invoice:
    """Represents a customer invoice."""

    invoice_id: str
    customer_name: str
    subtotal: float
    tax_rate: str  # Comes as string from CSV, e.g. '8.5'
    status: str = "pending"

    def total(self):
        """Calculate the total including tax."""
        from src.utils import calculate_total
        return calculate_total(self.subtotal, self.tax_rate)

    def summary(self):
        """Return a one-line summary of the invoice."""
        from src.utils import format_currency, normalize_name
        name = normalize_name(self.customer_name)
        return f"Invoice {self.invoice_id}: {name} — {format_currency(self.total)}"


@dataclass
class Customer:
    """Represents a customer record."""

    customer_id: str
    name: Optional[str]
    email: str
    tier: str = "standard"

    def display_name(self):
        """Get the display-ready customer name."""
        from src.utils import normalize_name
        return normalize_name(self.name)
