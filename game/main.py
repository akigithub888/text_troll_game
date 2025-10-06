from game.player import *
from game.world import *

def main():
    print("\n______________________\n\n🌴 Welcome to Stranglethorn Vale! 🌴\n______________________\n\n")
    print("You are a lost troll, deep in the jungle...\n")
    #print("Type 'quit' to quit the game.\n")

    player = Player("Troll", clearing)
    print(player.location.description)

    while True:
        loc = player.location
        if loc.enemy and loc.enemy.health > 0:
            player.combat_sequence(loc.enemy)
        print("\nExits:")
        for direction, destination in loc.exits.items():
            print(f"{direction} → {destination.name}")  # destination is also a Location
    
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