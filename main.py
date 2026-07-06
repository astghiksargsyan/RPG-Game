from models.game_manager import GameManager
from models.character import Character
def main():
    GameManager.start()
    print(Character.total_characters_count)
main()