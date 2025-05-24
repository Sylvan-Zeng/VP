SPECIES = ("dog", "cat", "pig", "chicken", "duck")
SOUNDS = {"dog": "Woof woof", "cat": "Meow meow", "pig": "HMM", "chicken": "Giggle", "duck": "Gaga"}

FOODS = {
    "cake":    {"hunger": -30, "happy": 5,  "clean": -7},
    "chocolate":    {"hunger": -20, "happy": 10,  "clean": -7},
    "fish":      {"hunger": -25, "happy": 15,  "clean": -5},
    "vegetable":    {"hunger": -15, "happy": -5, "clean": -2},
}
GAMES = {
    "ball":    {"happy": 15, "energy": -20, "hunger": 10, "clean": -5},
    "walk":    {"happy": 10, "energy": -15, "hunger": 10, "clean": -5},
    "hide-and-seek":  {"happy": 20, "energy": -25, "hunger": 15, "clean": -8},
}

class Pet:
    def __init__(self, name: str, species: str):
        self.name    = name
        self.species = species
        self.health = 100
        self.hunger = 0         # 0 = full; 100 = extremely hungry
        self.happy  = 50
        self.clean  = 100
        self.energy = 100
        self.alive  = True

    def clamp(self, attr: str):
        # Ensure that all attributes fall within the range of 0 to 100
        val = getattr(self, attr)
        setattr(self, attr, max(0, min(100, val)))

    def auto_decay(self):
        # Each round automatically decays: hunger, clean, energy, happy
        self.hunger += 5
        self.happy  -= 1
        self.clean -= 3
        self.energy -= 2
        for a in ("hunger", "happy", "clean", "energy"):
            self.clamp(a)
        print()
        print('auto decay:')
        print(f'hunger +5, {self.hunger:3d}/100')
        print(f'happy -1, {self.happy:3d}/100')
        print(f'clean -3, {self.clean:3d}/100')
        print(f'energy -2, {self.energy:3d}/100')

    def check_health(self):
        # Deduct health and check for death
        if self.hunger >= 100 or self.happy == 0 or self.clean == 0:
            self.health -= 10
            self.clamp("health")
            print(f'health -10, {self.health:3d}/100')
        if self.health == 0:
            self.alive = False

    def feed(self, food: str):
        if food not in FOODS:
            print("Unknown food!")
            return
        delta = FOODS[food]
        self.hunger += delta["hunger"]
        self.happy  += delta["happy"]
        self.clean  += delta["clean"]
        for a in ("hunger", "happy", "clean"):
            self.clamp(a)
        print(f'hunger {delta["hunger"]}, {self.hunger:3d}/100')
        print(f'happy {delta["happy"]}, {self.happy:3d}/100')
        print(f'clean {delta["clean"]}, {self.clean:3d}/100')

    def play(self, game: str):
        if self.energy < 20:
            print(f"{self.name} too tired to play...")
            return
        if game not in GAMES:
            print("Unknown ways of playing!")
            return
        delta = GAMES[game]
        self.hunger += delta["hunger"]
        self.happy  += delta["happy"]
        self.clean  += delta["clean"]
        self.energy += delta["energy"]
        for a in ("hunger", "happy", "clean", "energy"):
            self.clamp(a)
        print(f'hunger {delta["hunger"]}, {self.hunger:3d}/100')
        print(f'happy {delta["happy"]}, {self.happy:3d}/100')
        print(f'clean {delta["clean"]}, {self.clean:3d}/100')
        print(f'energy {delta["energy"]}, {self.energy:3d}/100')

    def bathe(self):
        self.clean = 100
        self.happy -= 5
        self.clamp("happy")
        print('The cleanliness has been restored.')
        print(f'happy -5, {self.happy:3d}/100')

    def sleep(self):
        self.energy = 100
        self.hunger += 15
        self.clamp("hunger")
        print('It is already full of energy.')
        print(f'hunger +15, {self.hunger:3d}/100')

    def give_medicine(self):
        self.health += 20
        self.hunger += 15
        self.happy  -= 10
        for a in ("health", "hunger", "happy"):
            self.clamp(a)
        print(f'health +20, {self.health:3d}/100')
        print(f'hunger +15, {self.hunger:3d}/100')
        print(f'happy -10, {self.happy:3d}/100')

    def round(self):
        # Automatic decay and health detection are carried out each round of execution
        self.auto_decay()
        self.check_health()

    def __str__(self) -> str:
        status = (
            f"name: {self.name}|specie: {self.species}|sound: {SOUNDS[self.species]}\n"
            f"hunger: {self.hunger:3d}/100\n"
            f"happy: {self.happy:3d}/100\n"
            f"clean: {self.clean:3d}/100\n"
            f"energy: {self.energy:3d}/100\n"
            f"health: {self.health:3d}/100"
        )
        return status
