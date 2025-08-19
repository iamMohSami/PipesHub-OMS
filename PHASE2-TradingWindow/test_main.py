import unittest
import datetime
from main import TradingWindow

class TestTradingWindow(unittest.TestCase):
    def test_trading_window(self):
        tw = TradingWindow(9, 15)
        morning = datetime.time(10, 0, 0)
        evening = datetime.time(16, 0, 0)
        self.assertTrue(tw.is_open(morning))
        self.assertFalse(tw.is_open(evening))

if __name__ == "__main__":
    unittest.main()
