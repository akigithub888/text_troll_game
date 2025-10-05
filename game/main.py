def main():
    print("🌴 Welcome to Stranglethorn Vale! 🌴")
    print("You are a lost troll, deep in the jungle...")
    print("Type 'quit' to exit.\n")

    while True:
        command = input("> ").strip().lower()

        if command == 'quit':
            print("You quit the game")
            break
        else:
            print(f"You said: {command} (nothing happens yet...)")



if __name__ == "__main__":
    main()