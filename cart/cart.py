"""Shopping cart: items, quantities, promo codes and the total in kopecks."""

from dataclasses import dataclass

PROMO_CODES = {
    "WELCOME10": 10,
    "FRIDAY25": 25,
}


@dataclass(frozen=True)
class Item:
    sku: str
    title: str
    price: int  # kopecks


class Cart:
    def __init__(self) -> None:
        self._lines: dict[str, tuple[Item, int]] = {}
        self._promo: str | None = None

    def add(self, item: Item, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        _, current = self._lines.get(item.sku, (item, 0))
        self._lines[item.sku] = (item, current + quantity)

    def remove(self, sku: str) -> None:
        self._lines.pop(sku, None)

    def apply_promo(self, code: str) -> None:
        if code not in PROMO_CODES:
            raise ValueError(f"unknown promo code: {code}")
        self._promo = code

    def subtotal(self) -> int:
        return sum(item.price * qty for item, qty in self._lines.values())

    def total(self) -> int:
        subtotal = self.subtotal()
        if self._promo is None:
            return subtotal
        discount = subtotal * PROMO_CODES[self._promo] // 100
        return subtotal - discount

    def __len__(self) -> int:
        return sum(qty for _, qty in self._lines.values())
