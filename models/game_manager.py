import random
from utils.file_operations import save_to_file
from models.character import Character
from models.player import Player
from models.mage import Mage
from models.warrior import Warrior
from models.archer import Archer
from models.enemy import Enemy
from models.monster import Monster
player = Player()
heroes = [Mage(), Warrior(), Archer()]
villains = [Enemy(), Monster()]

class GameManager:
    @staticmethod
    def start():
        """Start function"""
        player.collect_player_data()
        if player.character_type == "hero":
            hero = player.character
            enemy = random.choice(villains)
        else:
            hero = random.choice(heroes)
            enemy = player.character
        Player.battle(player, hero, enemy)
        save_to_file(player)
    @staticmethod
    def pc_choose_villain():
        """Randomly choose villain"""
        villain_choice = random.choice(villains)
        print(f"{villain_choice.name} is chosen")
        return villain_choice
    @staticmethod
    def pc_choose_hero():
        """Randomly choose hero"""
        hero_choice = random.choice(heroes)
        print(f"{hero_choice.name} is chosen")
        return hero_choice