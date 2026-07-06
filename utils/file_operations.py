import json
PLAYERS_LIST = "data/players.json"
def load_players():
    """Load the players from the file"""
    try:
        with open (PLAYERS_LIST, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_to_file(player):
    """Store the player information to the JSON file"""
    players = load_players()
    players.append(player.create_player_dict())
    with open (PLAYERS_LIST, "w", encoding="utf-8") as f:
            json.dump(players, f, indent = 4)
