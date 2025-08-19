from collections import defaultdict

class Order:
    def __init__(self, order_id, user_id, side, quantity, price):
        self.order_id = order_id
        self.user_id = user_id
        self.side = side  # "BUY" or "SELL"
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"{self.side} {self.quantity}@{self.price} (id={self.order_id})"

class OrderBook:
    def __init__(self):
        self.orders = {}  # order_id → Order
        self.buy_orders = []
        self.sell_orders = []

    def add_order(self, order: Order):
        if order.order_id in self.orders:
            return False
        self.orders[order.order_id] = order
        if order.side == "BUY":
            self.buy_orders.append(order)
            self.buy_orders.sort(key=lambda o: (-o.price, o.order_id))  # highest price priority
        else:
            self.sell_orders.append(order)
            self.sell_orders.sort(key=lambda o: (o.price, o.order_id))  # lowest price priority
        return True

    def cancel_order(self, order_id: str):
        if order_id not in self.orders:
            return False
        order = self.orders.pop(order_id)
        if order.side == "BUY":
            self.buy_orders = [o for o in self.buy_orders if o.order_id != order_id]
        else:
            self.sell_orders = [o for o in self.sell_orders if o.order_id != order_id]
        return True

    def modify_order(self, order_id: str, new_quantity: int, new_price: float):
        if order_id not in self.orders:
            return False
        order = self.orders[order_id]
        self.cancel_order(order_id)
        order.quantity = new_quantity
        order.price = new_price
        self.add_order(order)
        return True

    def get_order_book(self):
        return {
            "BUY": [str(o) for o in self.buy_orders],
            "SELL": [str(o) for o in self.sell_orders],
        }
