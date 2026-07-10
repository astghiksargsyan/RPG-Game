from models.character import Character

class Warrior(Character):
    """Class for Warrior characters."""
    name = "Warrior"
    def __init__(self,  health = 10, attack = 7, defense = 6):
        """Initialize a character with health, attack, and defense values."""
    def attack_function(self):
        """Perform the Warrior's attack action."""
        print("Warrior swings a sword!")
        self.health += 1
        self.attack += 2
        self.defense -= 3
        print(f"Warrior has the {self.health} health")
    def defense_function(self):
        """Perform the Warrior's defense action."""
        print("Warrior blocks with shield!")
        self.health -= 1
        self.defense -= 2
        print(f"Warrior has the {self.health} health")
    def special_function(self):
        """Perform the Warrior's unique special ability (Flame Strike)."""
        print("Warrior uses Flame Strike!")
        self.attack += 1
        self.health -= 2
        self.defense += 1
        print(f"Warrior has the {self.health} health")
    
