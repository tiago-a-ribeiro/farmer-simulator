import math

class Player:
    def __init__(self):
        self.energy = 100
        self.max_energy = 100
        self.inventory = []
        self.gold = 100

    #def get_task(self, task):
    #    return self.tasks[task]

    def get_gold(self):
        return self.gold

    def add_gold(self, amount):
        self.gold += amount
    
    def sub_gold(self, amount):
        self.add_gold(-amount)

    def consume_energy(self, consumption):
        if self.has_energy(consumption):
            self.energy = self.energy - consumption

    def has_energy(self, consumption):
        if (self.energy - consumption) < 0:
            print("INSUFFICIENT ENERGY")
            print("Your energy: " + str(self.energy))
            print("Energy required: " + str(consumption))
            return False
        else:
            return True

    def get_inventory_names(self):
        l = []
        for item in self.inventory:
            l.append(item.get_name())
        return l

    def add_inventory(self, new_item, amount):
        if new_item.get_name() in self.get_inventory_names():
            for item in self.inventory:
                if new_item.get_name() == item.get_name():
                    item.add_quantity(amount)
        else:
            self.inventory.append(new_item)
            for item in self.inventory:
                if new_item.get_name() == item.get_name():
                    item.add_quantity(amount - 1)
    
    def sub_inventory(self, item, amount):
        if item in self.inventory:
            index = self.inventory.index(item)
            self.inventory[index].min_quantity(amount)

    def get_inventory(self, item_name):
        for item in self.inventory:
            if item_name == item.get_name():
                if item.get_quantity() <= 0:
                    print("You do not have enough of that item")
                    return False
                else:
                    return item
        print("Item entered is not in you inventory")
        return False

    def is_in_inventory(self, item_name):
        for item in self.inventory:
            if item_name == item.get_name():
                return True
        print("Item: " + item_name + " is not in your inventory")
        return False

    def has_inventory(self, item_type):
        if self.inventory != []:
            for item in self.inventory:
                if item.get_type() == item_type:
                    return True
            print("You don't have any \'" + item_type + "s\'")
            return False
        else:
            print("Uh oh, looks like your inventory is empty, maybe try going to the SHOP to buy something!")
            return False

    def display_inventory(self, types):
        print("_______________________________")
        print("########## Inventory ##########")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
        for item in self.inventory:
            if types != []:
                if item.get_type() in types:
                    print(" " + item.name + ": " + str(item.get_quantity()) + " - $" + str(item.get_price()), end="; ")
            else:
                print(" " + item.name + ": " + str(item.get_quantity()) + " - $" + str(item.get_price()), end="; ")
        
        print(" ")
        print(" ")

    #def sort_inventory(self):
    #   this will eventually sort the players inventory

    def display_gold(self):
        print("Your Gold: $" + str(self.gold))

    def display_energy(self):
        meter = int(round(self.energy, -1) / 10)
        energy_bar = "|"
        for i in range(10):
            if meter > i:
                energy_bar = energy_bar + "#|"
            else:
                energy_bar = energy_bar + " |"

        print("         ___________________")
        print("Energy: " + energy_bar + " " + str(self.energy) + "/" + str(self.max_energy))
        print("         ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")