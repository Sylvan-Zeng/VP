from pet import Pet, SPECIES, SOUNDS, FOODS, GAMES

def choose_species() -> str:
    print("Optional pet species:", ", ".join(f"{i+1}.{sp}" for i, sp in enumerate(SPECIES)))
    while True:
        try:
            idx = int(input("Please select the pet specie number: ")) - 1
            if idx in range(len(SPECIES)):
                return SPECIES[idx]
        except ValueError:
            pass
        print("The input is invalid. Please reselect.")

def choose_name() -> str:
    while True:
        name = input("Please give your pet a name: ").strip()
        if name:
            return name
        print("The name cannot be empty.")

def show_menu():
    print("""
========= Command list =========
1. Feed
2. Play
3. Take a bath
4. Sleep
5. Take medicine
6. Check the status
0. Quit the game
============================
""")

def select_food() -> str:
    print("Optional foods:", ", ".join(FOODS.keys()))
    while True:
        food = input("What are you going to feed? ").strip()
        if food in FOODS:
            return food
        print("There is no such food!")

def select_game() -> str:
    print("Optional entertainments:", ", ".join(GAMES.keys()))
    while True:
        game = input("How do you want to play with it? ").strip()
        if game in GAMES:
            return game
        print("There is no such way to play!")

def main():
    print("=== Virtual pet ===")
    sp = choose_species()
    name = choose_name()
    pet = Pet(name, sp)
    print(f"Welcome {pet.name} ({pet.species}) join! {SOUNDS[sp]}~")

    while pet.alive:
        show_menu()
        cmd = input("Please enter the command number: ").strip()
        if cmd == "1":
            pet.feed(select_food())
        elif cmd == "2":
            pet.play(select_game())
        elif cmd == "3":
            pet.bathe()
        elif cmd == "4":
            pet.sleep()
        elif cmd == "5":
            pet.give_medicine()
        elif cmd == "6":
            print(pet)
        elif cmd == "0":
            print(pet)
            print("See you next time!")
            break
        else:
            print("Invalid instruction!")
            continue

        # Carry out automatic decay and health detection after each round
        pet.round()

    if not pet.alive:
        print()
        print(pet)
        print(f"It's a pity that {pet.name} has left us...")

if __name__ == "__main__":
    main()
