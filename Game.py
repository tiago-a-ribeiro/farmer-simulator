# Code beautifully crafted by Tiago Ribeiro
# I'm still trying to learn Python and I stuggled and learned quite a bit to make this program.
# Can't wait to look back at this in 5 years and realise how little I actually knew, and see how much I've grown since.
# 
# Farmer Simulator v0.1
# In this Farmer Simulator program you are a simple virtual farmer that will use commands
# to buy goods to be able to grow, harvest and sell crops to upgrade and pimp out your farm. 

import sys
from Item import Item
from Farm import Farm
from Player import Player
from Plant import Plant
from Seed import Seed
from Food import Food
from Shop import Shop
import copy

# This code only a little messy ;-;

tasks = {
        "TILL" : 2,
        "PLANT" : 3,
        "WATER" : 2,
        "HARVEST" : 1
}

harvest = {
    'BLUEBERRIES'  : Food("BLUEBERRIES",  50, 15),
    'STRAWBERRIES' : Food("STRAWBERRIES", 25, 10),
    'RASPBERRIES'  : Food("RASPBERRIES",  10, 8),
    'CORN'         : Food("CORN",         35, 20)
}

plants = {
    'BLUEBERRY'  : Plant('BLUEBERRY',  ['b', 'B'],  8, harvest['BLUEBERRIES']),
    'STRAWBERRY' : Plant('STRAWBERRY', ['s', 'S'],  5, harvest['STRAWBERRIES']),
    'RASPBERRY'  : Plant('RASPBERRY',  ['r', 'R'],  3, harvest['RASPBERRIES']),
    'CORN'       : Plant('CORN',       ['c', 'C'],  6, harvest['CORN'])
}

#put this in a json, learn that
items = {
    'seeds' : {
        'BLUEBERRY SEED'  : Seed("BLUEBERRY SEED",  10,  plants['BLUEBERRY']),
        'STRAWBERRY SEED' : Seed("STRAWBERRY SEED", 5,   plants['STRAWBERRY']),
        'RASPBERRY SEED'  : Seed("RASPBERRY SEED",  3,   plants['RASPBERRY']),
        'CORN SEED'       : Seed("CORN SEED",       7,   plants['CORN']),
    },
    'food' : {
        'BLUEBERRIES'     : Food("BLUEBERRIES",  50, 15),
        'STRAWBERRIES'    : Food("STRAWBERRIES", 25, 10),
        'RASPBERRIES'     : Food("RASPBERRIES",  10, 8),
        'CORN'            : Food("CORN",         35, 20)
    }
}

def input_error():
    print("Invalid Input")


def get_input():
    return input(">").upper()

def intro_message():
    print('')

def start():
    print(" _____                          _____ _           _     _                  ___   ___   ")
    print("|   __|___ ___ _____ ___ ___   |   __|_|_____ _ _| |___| |_ ___ ___    _ _|   | |_  |  ")
    print("|   __| .'|  _|     | -_|  _|  |__   | |     | | | | .'|  _| . |  _|  | | | | |_ _| |_ ")
    print("|__|  |__,|_| |_|_|_|___|_|    |_____|_|_|_|_|___|_|__,|_| |___|_|     \_/|___|_|_____|")
    print("")
    print("Welcome to Farmer Simulator v0.2 by Tiago Ribeiro!!! In this little program/game you will")
    print("get to till, water, plant and harvest on your own little virtual farm. This program is for me")
    print("to practice and experiment with python while also creating a (hopefully) fun game in the process")
    print("(btw, the idea for this game was born out of my chronic addiction to Stardew Valley)")
    print("")
    print("Please type: 'PLAY' or 'QUIT'")
    
    while (True):
        command = get_input()
        if (command == "PLAY"):
            game()
        elif (command == "QUIT"):
            sys.exit()
        else: 
            input_error()


def display_commands():
    print("")
    print("######################## COMMANDS #######################################")
    print("# COMMANDS   - shows this command list                                  #")
    print("# QUIT       - will exit the game                                       #")
    print("# DISPLAY    - displays your farm and energy                            #")
    print("# SHOP       - buy and sell goods at the shop                           #")
    print("# TILL       - till on a given plot                                     #")
    print("# WATER      - water on a given plot                                    #")
    print("# PLANT      - plant on a given plot                                    #")
    print("# HARVEST    - harvest your grown crops from a given plot               #")
    print("# BOXTILL    - till from given start and end plot                       #")
    print("# BOXPLANT   - plant from given start and end plot                      #")
    print("# BOXWATER   - water from given start and end plot                      #")
    print("# BOXHARVEST - harvest all crops from given start and end plot          #")
    print("# SLEEP      - regain energy and update your plants                     #")
    print("# UPGRADE    - make upgrades to your farm like increasing the width     #")
    print("#########################################################################")
    print("")


def game():
    intro_message()

    farm = Farm(5, 3)
    player = Player()
    shop = Shop()
    shop.generate_inventory(items['seeds'])

    display_commands()

    farm.display()
    player.display_energy()
    player.display_gold()
    player.display_inventory([])

    def boxing(task, item=None):
        farm.display()
        print("Please choose a starting plot")
        start = get_input()
        if farm.has_position(start):
            print("Please choose an ending point")
            end = get_input()

        valid_positions = farm.has_position(start) and farm.has_position(end)
                #Check if those positions are valid
        if valid_positions:
                #Check if player has energy to perform that many tills
            consumption = farm.get_boxconsumption(start, end, tasks[task])
            if player.has_energy(consumption):
                if farm.can_box(start, end, task, item):
                    player.consume_energy(consumption)
                    if task == "HARVEST":
                        return farm.box(start, end, task, item)
                    farm.box(start, end, task, item)

    
    while (True):
        print("So what would you like to do? (type a COMMAND)")
        command = get_input()

        if (command == "COMMANDS"):
            display_commands()

        elif (command == "QUIT"):
            sys.exit()

        elif (command == "DISPLAY"):
            farm.display()
            player.display_energy()
            player.display_gold()
            player.display_inventory([])

        elif (command == "TILL"):
            if player.has_energy(tasks[command]):
                print("Please type a position (ex: A1)")
                position = get_input()
                if farm.has_position(position):
                    if farm.till(position):
                        player.consume_energy(tasks[command])

        elif (command == "WATER"):
            if player.has_energy(tasks[command]):
                print("Please type a position (ex: A1)")
                position = get_input()
                if farm.has_position(position):
                    if farm.water(position):
                        player.consume_energy(tasks[command])

        elif (command == "PLANT"):
            if player.has_energy(tasks[command]):
                if player.has_inventory('seed'):
                    print("Please select a seed from inventory")
                    player.display_inventory(["seed"])
                    to_plant = get_input()
                        
                    #Input has to be a seed first
                    if to_plant in items['seeds']: 
                        if player.inventory != [] and player.is_in_inventory(to_plant):
                            seed = player.get_inventory(to_plant)
                            # Checking if player has enough of that seed
                            if seed != False:
                                print("Please type a position (ex: A1)")
                                position = get_input()

                                if farm.has_position(position):
                                    if farm.plant(position, seed.get_plant()):
                                        player.consume_energy(tasks[command])
                                        seed.min_quantity(1)
                    else:
                        print("Invalid seed given")
        
        elif (command == "HARVEST"):
            if player.has_energy(tasks[command]):
                print("Please type a position (ex: A1)")
                position = get_input()
                if farm.has_position(position):
                    #Check if there is a harvestable plant there
                    if farm.can_harvest(position):
                        harvest = farm.get_harvest(position)
                        if harvest != None:
                            harvest = copy.deepcopy(harvest)
                            player.add_inventory(harvest, 1)
                            player.consume_energy(tasks[command])
                        else:
                            print("Doesn't look like that plant is ready to harvest just yet.")

        elif (command == "BOXTILL"):
            boxing("TILL")

        elif (command == "BOXWATER"):
            boxing("WATER")

        elif (command == "BOXPLANT"):
            print("Please select a seed from your inventory (Make sure you have enough for the amount of plots you will plant on!)")
            player.display_inventory(["seed"])
            seed = get_input()
            if seed in items['seeds']:
                if player.is_in_inventory(seed): 
                    item = player.get_inventory(seed)
                    if item != False:
                        boxing("PLANT", item)
            else:
                print("Item entered is not a seed!")
             
        elif (command == 'BOXHARVEST'):
            harv = boxing('HARVEST')
            if harv != None or []:
                for h in harv:
                    food = copy.deepcopy(h)
                    player.add_inventory(food, 1)

        elif (command == 'SLEEP'):
            player.energy = 100
            farm.update()
            shop.generate_inventory(items['seeds'])
            print("You wake up feeling refreshed, ready to work hard another day!")
            farm.display()
            player.display_energy()
            player.display_gold()

        elif (command == 'SHOP'):
            print("")
            print("Welcome to my Shop! The name's Michael Malloy.")
            print("Please, browse my wares and see what you like!")
            print("")
            shop.display_commands()
            print("So would you like to buy? or sell maybe?")
            shop_input = get_input()

            while(shop_input != "EXIT"):
            
                if (shop_input == "EXIT"):
                    print("Goodbye, come again!")
                    break
                
                if (shop_input == "BUY"):
                    shop.display_inventory()
                    player.display_gold()
                    print("What do you want to buy?")
                    want = get_input()
                    if want in items['seeds'].keys():
                        the_item = copy.deepcopy(items['seeds'][want])
                        if want not in shop.get_inventory_names():
                            print("Woah there pal, I don't sell " + want)
                        else:
                            shop_item = shop.get_item(want)
                            print("So how many would you like?")
                            amount = get_input()
                            if not amount.isdigit():
                                print("Woah there, that ain't a number pal, try again.")
                            else:
                                amount = int(amount)
                                if not (amount > 0 and amount <= shop_item.get_quantity()):
                                    print("I'm sorry, I don't have that many of that item.")
                                else:
                                    price_to_pay = amount * shop_item.get_price()
                                    print("That'll be $" + str(price_to_pay) + ". Would you like to buy? (Y/N)")
                                    yn = get_input()
                                    while not (yn == 'Y' or yn == 'N'):
                                        print("Sorry, didn't quite catch that, the price is $" + str(price_to_pay) + ". Will you buy?(Y/N)")
                                        player.display_gold()
                                        yn = get_input()
                                    if yn == 'Y':
                                        if player.get_gold() < price_to_pay:
                                            print("Oh no! You don't have enough gold, maybe next time.")
                                        else:
                                            player.sub_gold(price_to_pay)
                                            shop_item.min_quantity(amount)
                                            player.add_inventory(the_item, amount)
                                            print("Pleasure doing business with you!")
                                    else:
                                        print("Ahhh, that's too bad.")

                elif (shop_input == 'SELL'):
                    print("This will eventually allow you to sell your items")
                    print("So what would you like to sell?")
                    player.display_inventory([])
                    to_sell = get_input()
                    if to_sell not in player.get_inventory_names():
                        print("Oh you don't have " + to_sell + " in your inventory")
                    else:
                        to_sell = player.get_inventory(to_sell)
                        print("How many would you like to sell?")
                        amount = get_input()
                        if not amount.isdigit():
                            print("Woah there that isn't a number!")
                        else:
                            amount = int(amount)
                            if not(amount > 0 and amount <= to_sell.get_quantity()):
                                print("Sorry, you don't have that many of that item.")
                            else:
                                to_sell.min_quantity(amount)
                                player.add_gold(to_sell.get_price() * amount)
                                print("You sold " + str(amount) + " " + to_sell.get_name() + "(s). You made $" + str(to_sell.get_price() * amount))
                
                else:
                    print("Not quite sure what \'" + shop_input + "\' means")
                

                print("So would you like to buy? or sell maybe?")
                shop_input = get_input()
               
                if (shop_input == "EXIT"):
                    print("Goodbye, come again!")
                    break
        
        elif (command == 'UPGRADE'):
            print("What kind of upgrade to you want to make?")
            print('##############################################')
            print('# WIDTH  - increase the width of your farm   #')
            print('# HEIGHT - icrease the height of your farm   #')
            print('##############################################')

            command = get_input()
            if (command == 'WIDTH'):
                price = farm.height ** 2 * 30 * farm.width
                print("To upgrade your farms WIDTH it will cost you: $" + str(price) + " gold")
                print("You have exactly: $" + str(player.get_gold()) + " gold")
                if player.get_gold() < price:
                    print("It looks like you don't have enough gold!!")
                else:
                    print("Are you sure you want to upgrade your farm's WIDTH? (Y/N)")
                    yn = get_input()
                    while not (yn == 'Y' or yn == 'N'):
                        print("Please type Y or N, yes or no")
                        print("Are you sure you want to upgrade your farm's WIDTH? (Y/N)")
                    if yn == 'Y':
                        farm.increase_width()
                        player.sub_gold(price)
                        print("Your farm's WIDTH is succesfully upgraded!")
                        print("You now have: $" + str(player.get_gold()) + " gold")
                    else:
                        print("Aww that's too bad")

            elif (command == 'HEIGHT'):
                price = farm.width ** 2 * 30 * farm.height
                print("To upgrade your farms HEIGHT it will cost you: $" + str(price) + " gold")
                print("You have exactly: $" + str(player.get_gold()) + " gold")
                if player.get_gold() < price:
                    print("It looks like you don't have enough gold!!")
                else:
                    print("Are you sure you want to upgrade your farm's HEIGHT? (Y/N)")
                    yn = get_input()
                    while not (yn == 'Y' or yn == 'N'):
                        print("Please type Y or N, yes or no")
                        print("Are you sure you want to upgrade your farm's HEIGHT? (Y/N)")
                    if yn == 'Y':
                        farm.increase_height()
                        player.sub_gold(price)
                        print("Your farms height is succesfully upgraded!")
                        print("You now have: $" + str(player.get_gold()) + " gold")
                    else:
                        print("Aww that's too bad")

            #print("This command should eventually upgrade the farm's height at a price")

        elif (command == 'ADD'):
            player.display_inventory([])
        
        else:
            input_error()


start()
