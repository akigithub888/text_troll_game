from game.player import *
from game.world import *

def main():
    print("\n______________________\n\n🌴 Welcome to Stranglethorn Vale! 🌴")
    print("You are a lost troll, deep in the jungle...")
    #print("Type 'quit' to quit the game.\n")

    player = Player("troll", clearing)

    while True:
        loc = player.location
        print(loc.description)
        if loc.enemy:
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
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()