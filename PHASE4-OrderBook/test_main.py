import unittest
from main import Order, OrderBook

class TestOrderBook(unittest.TestCase):
    def test_order_book(self):
        ob = OrderBook()
        o1 = Order("1", "u1", "BUY", 100, 50.0)
        o2 = Order("2", "u2", "SELL", 200, 55.0)
        o3 = Order("3", "u3", "BUY", 150, 52.0)

        self.assertTrue(ob.add_order(o1))
        self.assertTrue(ob.add_order(o2))
        self.assertTrue(ob.add_order(o3))

        book = ob.get_order_book()
        self.assertEqual(book["BUY"][0], str(o3))  # highest price buy comes first
        self.assertEqual(book["SELL"][0], str(o2))

        # Modify order
        ob.modify_order("1", 120, 56.0)
        book = ob.get_order_book()
        self.assertIn("56.0", book["BUY"][0])

        # Cancel order
        ob.cancel_order("2")
        book = ob.get_order_book()
        self.assertEqual(len(book["SELL"]), 0)

if __name__ == "__main__":
    unittest.main()
