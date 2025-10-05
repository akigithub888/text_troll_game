from game.world import *

class Player:
    def __init__(self, name, starting_location, health=20):
        self.name = name
        self.location = starting_location
        self.inventory = []
        self.health = health
        self.weapon = None

    def move(self, direction):
        if direction in self.location.exits:
            self.location = self.location.exits[direction]
            print(f"\nYou move {direction} to {self.location.name}.")
        else:
            print("You can't go that way!")