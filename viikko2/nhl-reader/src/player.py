class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.games = dict['games']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.penalties = dict['penalties']
        self.total_points = int(self.goals) + int(self.assists)

    def __str__(self):
        return f"{self.name:25}{self.team} {self.goals} + {self.assists} = {self.total_points}"
