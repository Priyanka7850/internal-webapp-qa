class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity=1):
        if product.id in self.items:
            self.items[product.id]['quantity'] += quantity
        else:
            self.items[product.id] = {'product': product, 'quantity': quantity}

    def remove_item(self, product):
        if product.id in self.items:
            del self.items[product.id]

    def update_quantity(self, product, quantity):
        if product.id in self.items:
            self.items[product.id]['quantity'] = quantity

    def get_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items.values())
