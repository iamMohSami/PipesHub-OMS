class UserSession:
    def __init__(self):
        self.logged_in_users = set()

    def logon(self, user_id: str) -> bool:
        if user_id in self.logged_in_users:
            return False
        self.logged_in_users.add(user_id)
        return True

    def logout(self, user_id: str) -> bool:
        if user_id not in self.logged_in_users:
            return False
        self.logged_in_users.remove(user_id)
        return True

    def is_logged_in(self, user_id: str) -> bool:
        return user_id in self.logged_in_users
