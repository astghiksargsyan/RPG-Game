from models.character import Character

class Monster(Character):
    """Class for Monster characters."""
    name = "Monster"
    def __init__(self):
        """Initialize the Monster character with health, attack, and defense values."""
        super().__init__(6, 9, 3)
    def attack_function(self):
        """Perform the Monster's attack action."""
        print("Monster slashes with sharp claws!")
        self.health += 1
        self.attack -= 2
        self.defense += 1
        print(f"Monster's has the {self.health} health")
    def defense_function(self):
        """Perform the Monster's defense action."""
        print("Monster hides in shadows!")
        self.health -= 1
        self.attack += 2
        self.defense -= 3
        print(f"Monster's has the {self.health} health")
    def special_function(self):
        """Perform the Monster's unique special ability (Bite Attack)."""
        print("Monster uses Bite Attack!")
        self.health -= 3
        self.attack += 2
        self.defense -= 3
        print(f"Monster's has the {self.health} health")