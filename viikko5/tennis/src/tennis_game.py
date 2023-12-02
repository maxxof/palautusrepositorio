class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1_score == self.player2_score:
            temp_score = self.player1_score
            if temp_score > 2:
                score = "Deuce"
            else:
                score = self.scores[temp_score] + "-All"

        elif self.player1_score >= 4 or self.player2_score >= 4:
            minus_result = self.player1_score - self. player2_score

            if minus_result == 1:
                score = f"Advantage {self.player1_name}"
            elif minus_result == -1:
                score = f"Advantage {self.player2_name}"
            elif minus_result >= 2:
                score = f"Win for {self.player1_name}"
            else:
                score = f"Win for {self.player2_name}"

        else:
            score = self.scores[self.player1_score] + "-" + self.scores[self.player2_score]

        return score
