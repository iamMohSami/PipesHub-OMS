import unittest
import time
from main import RateLimiter

class TestRateLimiter(unittest.TestCase):
    def test_rate_limiter(self):
        rl = RateLimiter(max_requests=2, window_seconds=2)
        self.assertTrue(rl.allow("user1"))
        self.assertTrue(rl.allow("user1"))
        self.assertFalse(rl.allow("user1"))  # too many
        time.sleep(2)
        self.assertTrue(rl.allow("user1"))   # window reset

if __name__ == "__main__":
    unittest.main()
