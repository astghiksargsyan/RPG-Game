import random
from abc import ABC, abstractmethod

class Character(ABC):
    """Base class for all game characters."""
    total_characters_created = 0
    name = "Character"
    def __init__(self, health, attack, defense):
        """Initialize a character with health, attack, and defense values."""
        self.health = health
        self.attack = attack
        self.defense = defense
        self.level = 1

        Character.total_characters_created += 1
    def is_alive(self):
        """Return True if the character is alive, otherwise False."""
        return self.health > 0 
    def take_damage(self, damage):
        """Reduce health when taking damage"""
        self.health -= damage
    def attack_enemy(self, enemy):
        """Attack another character"""
        damage = (self.attack - enemy.defense) // 2
        print(f"{self.name} attacks {enemy.name} | damage = {damage}")
        if damage > 0:
            enemy.take_damage(damage)
    @abstractmethod
    def attack_function(self):
        """Perform the character's attack action."""
        print(self.health)
    @abstractmethod
    def defense_function(self):
        """Perform the character's defense action."""
        print(self.health)
    @abstractmethod
    def special_function(self):
        """Perform the character's unique special ability."""
        print(self.health)
    @classmethod
    def total_characters_count(cls):
        """Returns the total characters count created during this game"""
        return cls.total_characters_created
    def choose_random_method(self):
        """Randomly choose and execute one of the character's actions."""
        functions_list = [
            self.attack_function,
            self.defense_function,
            self.special_function
        ]
        chosen_function = random.choice(functions_list)
        chosen_function()
    def __str__(self):
        """Human readable representation of Character"""
        return (
            f"Character: {self.name}\n"
            f"Health: {self.health}\n"
            f"Attack: {self.attack}\n"
            f"Defense: {self.defense}"
        )
    def __repr__(self):
        """Developement representation of Character"""
        return (
            f"{self.name} has the following scores:\n"
            f"Health: {self.health}\n"
            f"Attack: {self.attack}\n"
            f"Defense: {self.defense}"
        )