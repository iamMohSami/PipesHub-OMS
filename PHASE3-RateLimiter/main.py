import time

class RateLimiter:
    def __init__(self, max_requests=5, window_seconds=10):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}

    def allow(self, user_id: str) -> bool:
        now = time.time()
        if user_id not in self.requests:
            self.requests[user_id] = []
        # purge old
        self.requests[user_id] = [t for t in self.requests[user_id] if now - t < self.window_seconds]
        if len(self.requests[user_id]) < self.max_requests:
            self.requests[user_id].append(now)
            return True
        return False
