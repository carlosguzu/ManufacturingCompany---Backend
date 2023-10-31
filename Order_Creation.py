# Definition Class Order
class Order:
    def __init__(self, id, bottle_type, quantity, status):
        self.id = id
        self.bottle_type = bottle_type
        self.quantity = quantity
        self.status = status

    # Getter 'id'
    def get_id(self):
        return self.id

    # Setter 'id'
    def set_id(self, new_id):
        self.id = new_id

    # Getter 'bottle_type'
    def get_bottle_type(self):
        return self.bottle_type

    # Setter 'bottle_type'
    def set_bottle_type(self, new_bottle_type):
        self.bottle_type = new_bottle_type

    # Getter 'quantity'
    def get_quantity(self):
        return self.quantity

    # Setter 'quantity'
    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    # Getter 'status'
    def get_status(self):
        return self.status

    # Setter 'status'
    def set_status(self, new_status):
        self.status = new_status


