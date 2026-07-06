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

heros = [Mage(), Warrior(), Archer()]
villains = [Enemy(), Monster()]

class GameManager:
    @staticmethod
    def start():
        """Start function"""
        player.collect_player_data()
        if player.character_type == "hero":
            enemy = GameManager.pc_choose_villain()
            Player.battle(player, player.character, enemy)
        else:
            hero = GameManager.pc_choose_hero()
            Player.battle(player, hero, player.character)
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
        hero_choice = random.choice(heros)
        print(f"{hero_choice.name} is chosen")
        return hero_choice