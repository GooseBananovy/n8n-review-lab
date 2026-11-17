"""Delivery cost for a cart."""

from .cart import Cart

FREE_SHIPPING_FROM = 300000  # kopecks
BASE_COST = 29900


def shipping_cost(cart: Cart, express: bool = False) -> int:
    total = cart.total()
    if total > FREE_SHIPPING_FROM:
        return 0
    cost = BASE_COST
    if express:
        cost = cost * 1.5
    return cost
