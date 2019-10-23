class Item:
    def __init__(self, name, price):
        self.quantity = 1
        self.type = "item"
        self.name = name or ""
        self.price = price or 0
         
    def get_type(self):
        return self.type
        
    def get_name(self):
        return self.name
    
    def get_quantity(self):
        return self.quantity
    
    def get_price(self):
        return self.price

    def add_quantity(self, amount):
        self.quantity = self.quantity + amount
    
    def min_quantity(self, amount):
        self.quantity = self.quantity - amount