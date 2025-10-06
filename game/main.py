from game.player import *
from game.world import *

def main():
    print("🌴 Welcome to Stranglethorn Vale! 🌴")
    print("You are a lost troll, deep in the jungle...")
    print("Type 'quit' to exit.\n")

    player = Player("troll", clearing)

    while True:
        loc = player.location
        print(f"\nYou are at the {loc}\n")
        print(loc.description)
        if loc.enemy:
            player.combat_sequence(loc.enemy)
        print("Exits:")
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