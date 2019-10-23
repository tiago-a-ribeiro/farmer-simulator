from Item import Item

class Food(Item):
    def __init__(self, name, price, energy):
        super().__init__(name, price)
        self.energy = energy
        self.type = "food"
    
    def get_energy(self):
        return self.energy