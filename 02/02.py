import os


class Tournament:
    def __init__(self):
        self.loses_to = {}

    def add_match(self, playerA, playerB, winner_index):
        winner, loser = (playerA, playerB) if winner_index == "1" else (playerB, playerA)

        self.loses_to.setdefault(loser, []).append(winner)
        self.loses_to.setdefault(winner, [])

    def get_top_player(self):
        undefeated_player = min(self.loses_to.items(), key=lambda item: len(item[1]))
        return undefeated_player[0]


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    input_file = open("submitInput.txt", "r")
    num_cases = int(input_file.readline())
    output_file = open("submitOutput.txt", "w")

    for case in range(num_cases):
        num_matches = int(input_file.readline())
        tournament = Tournament()

        for _ in range(num_matches):
            tournament.add_match(*input_file.readline().split())

        output = f"Case #{case + 1}: {tournament.get_top_player()}\n"
        output_file.write(output)

    input_file.close()
    output_file.close()
