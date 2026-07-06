from models.character import Character
class Archer(Character):
    """Class for Archer characters."""
    name = "Archer"
    def __init__(self):
        """Initialize the Archer character with health, attack, and defense values."""
        super().__init__(5, 7, 2)
    def attack_function(self):
        """Perform the Archer's attack action."""
        print("Archer shoots an arrow!")
        self.health += 1
        self.attack -= 2
        self.defense -= 3
        print(f"Archer has the {self.health} health")
    def defense_function(self):
        """Perform the Archer's defense action."""
        print("Archer creates a  shield!!")
        self.health -= 1
        self.attack += 2
        self.defense += 3
        print(f"Archer has the {self.health} health")
    def special_function(self):
        """Perform the Archer's unique special ability (Shoots a fire arrow)."""
        print("Archer shoots a fire arrow!")
        self.health -= 1
        self.attack += 2
        self.defense += 1
        print(f"Archer has the {self.health} health")

