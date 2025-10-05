class Enemy:
    def __init__ (self, name, attack_power, weapon=None, health=10):
        self.name = name
        self.weapon = weapon
        self.attack_power = attack_power
        self.health = health

    
cannibal = Enemy("Cannibal", "spear", 10, 20)
panther = Enemy("Panther", 7)

