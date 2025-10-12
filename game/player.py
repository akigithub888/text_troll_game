from game.world import *
from game.enemies import *
from game.ui import *
import random
import sys


class Player:
    def __init__(self, name, starting_location, health=20, attack =15):
        self.name = name
        self.location = starting_location
        self.inventory = []
        self.health = health
        self.weapon = None
        self.attack = attack
        self.combat = False
        self.previous_location = starting_location

    def look(self):
        if self.location.items:
            item = self.location.items[0]
            print(f"\nYou look around for anything usable and you find a {item.name}\n")
        else:
            print(f"\nYou find nothing...\n")

    def pick_up_weapon(self, weapon):
        self.weapon = weapon
        current_attack = self.attack + weapon.attack
        print(f"You picked up the {weapon.name} and equipped it. Your attack is now {current_attack }")

    def pick_up_food(self, food):
        self.inventory.append(food)

    def pick_up_item(self, item):
        if isinstance(item, Food):
            self.pick_up_food(item)
        elif isinstance(item, Weapon):
            self.pick_up_weapon(item)

    def use_item(self, item):
        if isinstance(item, Food):
            self.health += item.heal_amount
        #add options if you add non food items       

    def move(self, direction):
        if direction in self.location.exits:
            self.previous_location = self.location
            self.location = self.location.exits[direction]
            #print(f"\nYou move {direction} to the {self.location.name}.")
            show_movement(direction, self.location.name)
        else:
            print("You can't go that way!")
    
    def describe_location(self):
        print(f"\nYou are at the {self.location.name}.")
        print(self.location.description)
        for direction, destination in self.location.exits.items():
            print(f"{direction} → {destination.name}")

    def status(self):
        return f"{self.name} — HP: {self.health}"
    
    def combat_sequence(self, enemy):
        #print(f"\nA wild {enemy.name} attacks you\n")
        show_combat_intro(enemy)
        round_number = 1
        while self.health > 0 and enemy.health > 0:
            print("-------------------------")
            print(f"Round {round_number}:\n")
            print(self.status())
            print(enemy.status())
            command = input("> ").strip().lower()
            if command == 'attack':
                player_attack = self.attack
                if self.weapon:
                    player_attack += self.weapon.attack
                enemy.health -= player_attack
                print(f"\nYou attack the {enemy.name} for {player_attack} damage")
                self.health = max(self.health, 0)
                if enemy.health <= 0:
                    print(f"\nYou have defeated the {enemy.name}.\n")
                    break
        
                enemy_attack = enemy.attack
                self.health -= enemy_attack
                enemy.health = max(enemy.health, 0)
                print(f"\nThe {enemy.name} attacks you for {enemy_attack} damage")

                if self.health <= 0:
                    print(f"\nYou have died.")
            elif command == "flee":
                if random.random() < 0.5:
                    self.location = self.previous_location
                    print(f"You ran away successfully")
                    self.describe_location()
                    break
                else:
                    self.health -= 5
                    print(f"\nYou tripped and failed to flee")

            elif command.startswith("use "):
                item = command.split()[1]
                if isinstance(item, Item):
                    self.use_item(item)
                else:
                    print(f"{item} not in available")

            elif command == 'quit':
                print("You run back to safety. Game over!")
                sys.exit()
                break
            else:
                print("Unknown command.")
            round_number += 1


            

        
        
