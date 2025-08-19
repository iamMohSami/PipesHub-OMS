import unittest
from main import UserSession

class TestUserSession(unittest.TestCase):
    def test_login_logout(self):
        session = UserSession()
        self.assertTrue(session.logon("user1"))
        self.assertTrue(session.is_logged_in("user1"))
        self.assertFalse(session.logon("user1"))  # duplicate
        self.assertTrue(session.logout("user1"))
        self.assertFalse(session.is_logged_in("user1"))

if __name__ == "__main__":
    unittest.main()
