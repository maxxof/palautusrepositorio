import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_searching_by_name_gives_right_player(self):
        name = "Gretzky"
        player = self.stats.search(name)

        self.assertAlmostEqual(name, player.name)
    
    def test_searching_returns_none_if_wrong_name(self):
        name = "Max"
        player = self.stats.search(name)

        self.assertAlmostEqual(player, None)

    def test_teamsearch_gives_all_team_members(self):
        team = "EDM"
        right_names = sorted(["Semenko", "Kurri", "Gretzky"])

        players = self.stats.team(team)
        players_names = sorted([player.name for player in players])

        self.assertAlmostEqual(right_names[0], players_names[0])
        self.assertAlmostEqual(right_names[1], players_names[1])
        self.assertAlmostEqual(right_names[2], players_names[2])

    def test_top_players_sorting_by_points_right(self):
        top = self.stats.top(3)
        top1 = top[0]
        top2 = top[1]
        top3 = top[2]

        self.assertGreater(top1.points, top2.points)
        self.assertGreater(top2.points, top3.points)

    def test_top_players_sorting_by_goals_right(self):
        top = self.stats.top(3, SortBy.GOALS)
        
        self.assertGreater(top[0].goals, top[1].goals)
        self.assertGreater(top[1].goals, top[2].goals)

    def test_top_players_sorting_by_assists_right(self):
        top = self.stats.top(3, SortBy.ASSISTS)

        self.assertGreater(top[0].assists, top[1].assists)
        self.assertGreater(top[1].assists, top[2].assists)


    


        
