class ShoppingCart(object):
    def __init__(self):
        self.total = 0
        self.items = {}

    def add_item(self, item_name, quantity, price):
        self.total += price * quantity
        previous_quantity = self.items.get(item_name, 0)
        self.items[item_name] = quantity + previous_quantity

    def remove_item(self, item_name, quantity, price):
        if item_name in self.items:
            if quantity > self.items[item_name]:
                quantity = self.items[item_name]

            self.total -= quantity * price
            self.items[item_name] = self.items[item_name] - quantity
            if self.items[item_name] == 0:
                del self.items[item_name]

        else:
            raise KeyError(item_name)

    def checkout(self, cash_paid):
        if cash_paid < self.total:
            return 'Cash paid not enough'
        return cash_paid - self.total


class Shop(ShoppingCart):
    def __init__(self):
        super(Shop, self).__init__()
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1

import unittest;

class Test(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()
        self.shop = Shop()

    def test_cart_property_initialization(self):
        self.assertEqual(self.cart.total, 0, msg='Initial value of total not correct')
        self.assertIsInstance(self.cart.items, dict, msg='Items is not a dictionary')

    def test_add_item(self):
        self.cart.add_item('Mango', 3, 10)
        self.assertEqual(self.cart.total, 30, msg='Cart total not correct after adding items')
        self.assertEqual(self.cart.items['Mango'], 3, msg='Quantity of items not correct after adding item')

    def test_add_item_hidden(self):
        self.cart.add_item('Mango', 3, 10)
        self.cart.add_item('Orange', 16, 10)
        self.assertEqual(self.cart.total, 190, msg='Cart total not correct after adding items')
        self.assertEqual(self.cart.items['Orange'], 16, msg='Quantity of items not correct after adding item')

    def test_remove_item(self):
        self.cart.add_item('Mango', 3, 10)
        self.cart.remove_item('Mango', 2, 10)
        self.assertEqual(self.cart.total, 10, msg='Cart total not correct after removing item')
        self.assertEqual(self.cart.items['Mango'], 1, msg='Quantity of items not correct after removing item')

    def test_remove_item_hidden(self):
        self.cart.add_item('Mango', 3, 10)
        self.cart.add_item('Orange', 16, 10)
        self.cart.remove_item('Mango', 2, 10)
        self.assertEqual(self.cart.total, 170, msg='Cart total not correct after removing item')
        self.assertEqual(self.cart.items['Mango'], 1, msg='Quantity of items not correct after removing item')
        self.cart.remove_item('Mango', 2, 10)
        self.assertEqual(self.cart.total, 160, msg='Cart total not correct after removing item')
        with self.assertRaises(KeyError):
            self.cart.items['Mango']

    def test_checkout_returns_correct_value(self):
        self.cart.add_item('Mango', 3, 10)
        self.cart.add_item('Orange', 16, 10)
        self.assertEqual(self.cart.checkout(265), 75, msg='Balance of checkout not correct')
        self.assertEqual(self.cart.checkout(25), 'Cash paid not enough', msg='Balance of checkout not correct')


    def test_shop_is_instance_of_shopping_cart(self):
        self.assertTrue(isinstance(self.shop, ShoppingCart), msg='Shop is not a subclass of ShoppingCart')

    def test_shop_initializaton(self):
        self.assertEqual(self.shop.quantity, 100, msg='Shop quantity not initialized correctly')

    def test_shop_remove_item_method(self):
        for i in range(15):
            self.shop.remove_item()

        self.assertEqual(self.shop.quantity, 85)