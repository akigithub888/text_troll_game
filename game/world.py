from game.enemies import *


class Location:
    def __init__(self, name, description, exits=None, items=None, enemy=None):
        self.name = name
        self.description = description
        self.exits = exits if exits else {}   # dictionary: direction -> Location
        self.items = items if items else []   # list of items
        self.enemy = enemy                    # Enemy instance or None

    def add_exit(self, direction, location):
        self.exits[direction] = location

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return self.name  

clearing = Location("Clearing", "A small jungle clearing. You hear beasts nearby.")
riverbank = Location("Riverbank", "The river flows swiftly. Crocolisks lurk in the water.", items=["spear"])
cannibal_camp = Location("Cannibal Camp", "A cannibal camp! Smells terrible.", enemy=cannibal)

clearing.add_exit("north", riverbank)
clearing.add_exit("east", cannibal_camp)
riverbank.add_exit("south", clearing)
cannibal_camp.add_exit("west", clearing)
