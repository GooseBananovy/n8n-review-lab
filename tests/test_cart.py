import unittest

from cart import Cart, Item

TEA = Item("tea", "Green tea", 35000)
MUG = Item("mug", "Mug", 50000)


class CartTest(unittest.TestCase):
    def test_empty_cart(self):
        cart = Cart()
        self.assertEqual(cart.total(), 0)
        self.assertEqual(len(cart), 0)

    def test_quantities_add_up(self):
        cart = Cart()
        cart.add(TEA)
        cart.add(TEA, 2)
        self.assertEqual(len(cart), 3)
        self.assertEqual(cart.subtotal(), 105000)

    def test_non_positive_quantity_rejected(self):
        with self.assertRaises(ValueError):
            Cart().add(TEA, 0)

    def test_remove(self):
        cart = Cart()
        cart.add(TEA)
        cart.add(MUG)
        cart.remove("tea")
        self.assertEqual(cart.total(), 50000)

    def test_promo_discount(self):
        cart = Cart()
        cart.add(MUG, 2)
        cart.apply_promo("WELCOME10")
        self.assertEqual(cart.total(), 90000)

    def test_unknown_promo_rejected(self):
        with self.assertRaises(ValueError):
            Cart().apply_promo("FREE100")


if __name__ == "__main__":
    unittest.main()
