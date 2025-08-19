import datetime

class TradingWindow:
    def __init__(self, start_hour=9, end_hour=15):
        self.start_hour = start_hour
        self.end_hour = end_hour

    def is_open(self, current_time=None) -> bool:
        if current_time is None:
            current_time = datetime.datetime.now().time()
        return self.start_hour <= current_time.hour < self.end_hour
