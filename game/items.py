class Item:
    def __init__(self, name):
        self.name = name

class Weapon(Item):
    def __init__(self, name, attack):
        super().__init__(name)
        self.attack = attack

    def details(self):
        print(f"\n...\nWeapon: {self.name}, Attack: {self.attack}\n...")

class Food(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name)
        self.heal_amount = heal_amount

    def details(self):
        print(f"\n...\Food: {self.name}, Heal Amount: {self.heal_amount}\n...")



spear = Weapon("spear", attack=3)
questionable_meat = Food("questionable meat", heal_amount=10)