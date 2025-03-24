class Checkout:
    def __init__(self, cart, user):
        self.cart = cart
        self.user = user
        self.order = None

    def process_order(self):
        if not self.cart.items:
            raise ValueError("Cart is empty")
        self.order = Order(user=self.user, items=self.cart.items.values(), total=self.cart.get_total())
        self.cart.items.clear()
        return self.order
