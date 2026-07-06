from models.character import Character

class Mage(Character):
    """Class for Mage characters."""
    name = "Mage"
    def __init__(self):
        """Initialize the Mage character with health, attack, and defense values."""
        super().__init__(26, 12, 16)
    def attack_function(self):
        """Perform the Mage's attack action."""
        print("Mage casts a magic bolt!")
        self.health += 1
        self.attack -= 2
        self.defense -= 3
        print(f"Mage has the {self.health} health")
    def defense_function(self):
        """Perform the Mage's defense action."""
        print("Mage creates a magical shield!")
        self.health -= 1
        self.attack += 2
        self.defense -= 3
        print(f"Mage has the {self.health} health")
    def special_function(self):
        """Perform the Mage's unique special ability (Casts ultimate spell)."""
        print("Mage casts ultimate spell!")
        self.health -= 2
        self.attack += 1
        self.defense += 1
        print(f"Mage has the {self.health} health")