import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._response = requests.get(url).json()
        self._players = self.base_players()

    def base_players(self):
        players = []
        for player_dict in self._response:
            player = Player(player_dict)
            players.append(player)
        return players

    def get_players(self):
        return self._players
