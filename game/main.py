from game.player import *
from game.world import *
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress
from rich.text import Text
from game.ui import show_location, show_items, enemy_info, show_intro



def main():
    
    show_intro()
    

    player = Player("Troll", clearing)

    while True:
        loc = player.location
        if loc.enemy and loc.enemy.health > 0:
            player.combat_sequence(loc.enemy)
        show_location(loc)
    
        command = input("> ").strip().lower()

        if command == 'quit':
            print("You run back to safety. Game over!")
            break
        elif command.startswith("go "):
            direction = command.split()[1]
            player.move(direction)
        elif command == "look":
            player.look()
        elif command.startswith("pick up "):
            item_name = " ".join(command.split()[2:])  # captures all words after 'pick up'
            found_item = None
            for obj in loc.items:
                if obj.name.lower() == item_name.lower():  # case-insensitive match
                    found_item = obj
                    break
            if found_item:
                player.pick_up_item(found_item)
                loc.items.remove(found_item) # remove item from room
                print(f"You picked up the {found_item.name}")
            else:
                print(f"{item_name} not found")

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()