from models.game_manager import GameManager
from models.archer import Archer
from models.warrior import Warrior
from models.mage import Mage
from models.monster import Monster
from models.enemy import Enemy
heroes = [Mage(), Warrior(), Archer()]
villains = [Enemy(), Monster()]
def main():
    while True:
        print("1. Start Game")
        print("2. Show Characters")
        print("3. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            GameManager.start()
        elif choice == "2":
            print("You can choose from heroes:")
            for hero in heroes:
                print(hero.name)
            print("Or you can choose from villains:")
            for villain in villains:
                print(villain.name)
        elif choice == "3":
            break
        else:
            print("Invalid option")
main()