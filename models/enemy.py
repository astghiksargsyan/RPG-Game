from models.character import Character

class Enemy(Character):
    """Class for Enemy characters."""
    name = "Enemy"
    def __init__(self,  health = 15, attack = 7, defense = 6):
        """Initialize the Enemy character with health, attack, and defense values."""
    def attack_function(self):
        """Perform the Enemy's attack action."""
        print("Enemy fires a gun!")
        self.health -= 1
        self.attack -= 2
        self.defense += 3
        print(f"Enemy has the {self.health} health")
    def defense_function(self):
        """Perform the Enemy's defense action."""
        print("Enemy takes cover!")
        self.health -= 1
        self.attack += 2
        self.defense -= 3
        print(f"Enemy has the {self.health} health")
    def special_function(self):
        """Perform the Monster's unique special ability (Heavy fire)."""
        print("Enemy uses heavy fire!")
        self.health -= 1
        self.attack += 2
        self.defense += 1
        print(f"Enemy has the {self.health} health")
    