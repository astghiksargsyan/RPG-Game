from models.archer import Archer
from models.warrior import Warrior
from models.mage import Mage
from models.monster import Monster
from models.enemy import Enemy

class Player():
    """Player class for managing player's information"""
    def __init__(self):
        """initial information for player"""
        self.name = ""
        self.character = None
        self.score = 0
        self.character_type = ""
    def collect_player_data(self):
        """Collect information of player name and character and character type for performing further action"""
        self.name = input("Enter your name: ")
        self.character_type = input("Choose a character type (hero or villain): ").lower()
        if self.character_type == "hero":
            hero_choice = input("Choose a hero (Archer, Mage, or Warrior): ").lower()
            self.character = self.choose_hero(hero_choice)
        elif self.character_type == "villain":
            villain_choice = input("Choose a villain (Enemy or Monster): ").lower()
            self.character = self.choose_villain(villain_choice)
        else:
            print("Invalid choice. Please choose either a hero or a villain.")
        return self.character
    @staticmethod
    def type_of_hero_action(char):
        """Handles player's chosen action during their turn."""
        type_of_action = input("Choose the type of action (attack / defense / special function): ").lower()
        if type_of_action == "attack":
            char.attack_function()
            print(f"{char.name} used attack!")
        elif type_of_action == "defense":
            char.defense_function()
            print(f"{char.name} used defense!")
        elif type_of_action == "special function":
            char.special_function()
            print(f"{char.name} used special function!")
        else:
            print("Invalid action.")  
    @staticmethod
    def battle(player, hero, enemy):
        while hero.is_alive() or enemy.is_alive():
            print("\n--- HERO TURN ---")
            Player.type_of_hero_action(hero)
            hero.attack_enemy(enemy)
            if not enemy.is_alive():
                player.score += 1
                print(f"{enemy.name} is defeated!")
                print(f"Hero wins! Score: {player.score}")
                break
            print("\n--- ENEMY TURN ---")
            enemy.choose_random_method()
            enemy.attack_enemy(hero)
            if not hero.is_alive():
                print(f"{hero.name} is defeated!")
                print(f"Enemy wins! Score: {player.score}")
                break
    @staticmethod
    def choose_hero(choice):
        """Chose for the type of the hero"""
        if choice == "archer":
            return Archer()
        elif choice == "mage":
            return Mage()
        elif choice == "warrior":
            return Warrior()
        else:
            print("Invalid character choice.")
    @staticmethod
    def choose_villain(choice):
        """Choose the type of villain."""
        if choice == "monster":
            return Monster() 
        elif choice == "enemy":
             return Enemy()
        else:
            print("Invalid character choice.")
    def create_player_dict(self):
        """Create a dictionary representation of the player for JSON saving."""
        tmp = {}
        tmp["name"] = self.name
        tmp["score"] = self.score
        tmp["type"] = self.character.name
        return tmp