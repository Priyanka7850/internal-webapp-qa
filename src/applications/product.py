

class Product:
    def __init__(self, id, name, description, price, stock):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("Not enough stock available")
        self.stock -= quantity
