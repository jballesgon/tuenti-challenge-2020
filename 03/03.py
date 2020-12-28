import operator
import os
import re
from collections import defaultdict


class BookParser:
    def __init__(self, book):
        self.word_frequencies = self.parse_book(book)
        self.word_ranking = self.rank_words(self.word_frequencies)

    def parse_book(self, book):
        parsed_book = re.sub(r"[^a-záéíóúüñ]", " ", book.lower())
        valid_words = [word for word in parsed_book.split() if len(word) > 2]

        word_frequencies = defaultdict(int)
        for word in valid_words:
            word_frequencies[word] += 1

        return word_frequencies

    def rank_words(self, word_frequencies):
        sorted_by_word = sorted(word_frequencies.items())
        sorted_by_frequency = sorted(sorted_by_word, key=operator.itemgetter(1), reverse=True)
        return [item[0] for item in sorted_by_frequency]

    def get_word_data(self, word):
        return (self.word_ranking.index(word) + 1, self.word_frequencies[word])

    def get_word_data_in_rank(self, rank):
        word = self.word_ranking[rank - 1]
        return (word, self.word_frequencies[word])


if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    book = open("pg17013.txt", "r")
    parsed_book = BookParser(book.read())
    book.close()

    input_file = open("submitInput.txt", "r")
    input_file.readline()
    output_file = open("submitOutput.txt", "w")

    for index, line in enumerate(input_file):
        case_input = line.rstrip()

        if case_input.isdigit():
            word, frequency = parsed_book.get_word_data_in_rank(int(case_input))
            output = f"{word} {frequency}"
        else:
            rank, frequency = parsed_book.get_word_data(case_input)
            output = f"{frequency} #{rank}"

        output_file.write(f"Case #{index + 1}: {output}\n")

    input_file.close()
    output_file.close()
