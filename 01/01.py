import os


RPS_pairs = {
    frozenset(["R", "P"]): "P",
    frozenset(["R", "S"]): "R",
    frozenset(["S", "P"]): "S",
}


def play_RPS(hand1, hand2):
    pair_set = frozenset([hand1, hand2])
    return RPS_pairs[pair_set] if len(pair_set) == 2 else "-"


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    input_file = open("submitInput.txt", "r")
    input_file.readline()
    output_file = open("submitOutput.txt", "w")

    for index, line in enumerate(input_file):
        result = play_RPS(*line.split())
        output_file.write(f"Case #{index + 1}: {result}\n")

    input_file.close()
    output_file.close()
