import random
import copy

class Shop:
    def __init__(self):
        self.inventory = []
        
    def get_inventory(self):
        return self.inventory

    def get_item(self, want):
        for item in self.inventory:
            if item.get_name() == want:
                return item

    def get_item_quantity(self, item_name):
        for item in self.inventory:
            if item.get_name() == item_name:
                print(item.get_quantity())
                return item.get_quantity()
        return None
    
    def get_item_price(self, item_name):
        for item in self.inventory:
            if item.get_name() == item_name:
                print(item.get_price())
                return item.get_price()
        return None

    def get_inventory_names(self):
        result = []
        for item in self.inventory:
            result.append(item.get_name())
        return result

    def buy_item(self, item):
        print("This should buy from the shop")

    def generate_inventory(self, items):
        self.inventory = []
        choices = []
        choice = random.choice(list(items.keys()))
        choices.append(choice)
        num = 1

        while (num < 3):
            choice = random.choice(list(items.keys()))
            if choice in choices:
                # Don't add that item if we already have it
                continue
            else:
                choices.append(choice)
                num += 1
        
        for key in choices:
            item = copy.deepcopy(items[key])
            amount = random.randint(5, 10)
            item.add_quantity(amount)
            self.inventory.append(item)
    
    def sub_inventory(self, name, amount):
        for item in self.inventory:
            if item.get_name() == name:
                item.min_quantity(amount)
                print(item.get_quantity())
                if item.get_quantity() <= 0:
                    del item

    def display_commands(self):
        print("##################### SHOP COMMANDS ####################")
        print("# EXIT - to leave the shop                             #")
        print("# BUY  - purchase a given number of items              #")
        print("# SELL - sell any amount of an item in your inventory  #")
        print("########################################################")
        print("")

    def display_inventory(self):
        print("")
        print("#######################")
        print("# SHOP: ###############")
        print("")
        
        for item in self.inventory:
            print(item.get_name() + "(Q:" + str(item.get_quantity()) + ") - $" + str(item.get_price()), end = "; ")    
        
        print("")
        print("")
        print("#######################")
        print("")
