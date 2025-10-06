class Enemy:
    def __init__ (self, name, attack, weapon=None, health=10):
        self.name = name
        self.weapon = weapon
        self.attack = attack
        self.health = health

    def status(self):
        return f"{self.name} — HP: {self.health}"

    
cannibal = Enemy("Cannibal", weapon="spear", attack=10, health=20)
crocolisk = Enemy("Crocolisk", attack=7, health=10)

