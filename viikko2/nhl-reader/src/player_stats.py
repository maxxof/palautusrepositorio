class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        nationality_players = [player for player in self._players if player.nationality == nationality]
        toplist = sorted(nationality_players, key=lambda player: player.total_points, reverse=True)
        return toplist

