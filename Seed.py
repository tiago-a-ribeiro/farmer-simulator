from Item import Item
from Plant import Plant
from Food import Food
import copy

class Seed(Item):
    def __init__(self, name, price, plant):
        super().__init__(name, price)
        self.plant = plant
        self.type = "seed"

    def get_plant(self):
        return copy.deepcopy(self.plant)


