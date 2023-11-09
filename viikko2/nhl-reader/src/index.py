import requests
from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    reader = PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players")
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()