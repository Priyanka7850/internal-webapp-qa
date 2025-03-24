class Order:
    def __init__(self, user, items, total):
        self.user = user
        self.items = items
        self.total = total
        self.status = 'Pending'

    def complete_order(self):
        self.status = 'Completed'
