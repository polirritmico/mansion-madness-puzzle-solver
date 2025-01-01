#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class PuzzleSolver:
    symbols: list[str]
    size: int
    seed: int
    possibilities: list[list[str]]
    evidence: list  # check this

    def __init__(self, symbols: list[str], seed: int = None):
        self.symbols = symbols
        self.size = len(symbols)
        assert self.size > 1

        if seed is not None:
            self.seed = seed
        else:
            self.seed = random.randint(0, 99999)
        random.seed(self.seed)

        self.possibilities = self.generate_all_guesses(self.size, self.symbols)
        self.evidence = []

    def generate_all_guesses(self, size, items) -> None:
        assert size >= 1

        if size == 1:
            return [[symbol] for symbol in items]

        suffixes = self.generate_all_guesses(size - 1, items)
        return [[symbol] + suffix for symbol in items for suffix in suffixes]

    def guess_contradicts_some_evidence(self, guess):
        for case in self.evidence:
            judgment = self.judge_guess(guess, case["guess"])
            if judgment != {
                "both_correct": case["both_correct"],
                "symbol_correct": case["symbol_correct"],
            }:
                return True
        return False

    def judge_guess(self, answer, guess):
        ret_val = {"both_correct": 0, "symbol_correct": 0}
        unacounted_answers = []
        unacounted_guesses = []
        for a, g in zip(answer, guess):
            if a == g:
                ret_val["both_correct"] += 1
            else:
                unacounted_answers.append(a)
                unacounted_guesses.append(g)

        for ua in unacounted_answers:
            if ua in unacounted_guesses:
                ret_val["symbol_correct"] += 1
                unacounted_guesses.remove(ua)

        return ret_val

    def next_guess(self) -> list[str]:
        while self.possibilities:
            guess = self.possibilities.pop(
                random.randint(0, len(self.possibilities) - 1)
            )
            if not self.guess_contradicts_some_evidence(guess):
                return guess
        return None

    def evaluate_results(
        self, case, both_good: int | None = None, symbol_good: int | None = None
    ) -> bool:
        if both_good is None:
            both_good = int(
                input("Enter number of correct symbols in correct positions: ") or 0
            )
        if both_good == self.size:
            return True
        if symbol_good is None:
            symbol_good = int(
                input("Enter number of correct symbols in wrong positions: ") or 0
            )
        self.evidence.append(
            {
                "guess": case,
                "both_correct": both_good,
                "symbol_correct": symbol_good,
            }
        )
        return False

    def solve(self) -> None:
        # global_game_state = {
        #     "num_pegs": num_pegs,
        #     "symbols": symbols,
        #     "possible_guesses": possible_guesses,
        # }

        while True:
            if not self.possibilities:
                print("No more possible guesses. Probably an error in your inputs.")
                break
            guess = self.next_guess()
            if guess is None:
                print("Ran out of possible guesses.")
                break
            print(f"Next guess: {',  '.join(guess)}")

            if self.evaluate_results(guess):
                print("Solved!")
                break

            # both_correct = int(
            #     input("Enter number of correct symbols in correct positions: ")
            # )
            # if both_correct == self.size:
            #     print("Solved!")
            #     break
            #
            # symbol_correct = int(
            #     input("Enter number of correct symbols in wrong positions: ")
            # )
            #
            # self.evidence.append(
            #     {
            #         "guess": guess,
            #         "both_correct": both_correct,
            #         "symbol_correct": symbol_correct,
            #     }
            # )


# def main():
#     print("Mansion of Madness Puzzle Solver")
#     # num_pegs = int(input("Number of symbols?: "))
#     # symbols = input("Enter symbols (comma-separated): ").split(",")
#     seed = random.randint(0, 9999)
#     random.seed(seed)
#     print(f"Using random seed: {seed}")
#     num_pegs = 5
#     # symbols = "1, 2, 3, 4, 5"
#     symbols = "r, y, g, b, o".split(",")
#
#     possible_guesses = generate_all_guesses(num_pegs, symbols)
#     global global_game_state
#     global_game_state = {
#         "num_pegs": num_pegs,
#         "symbols": symbols,
#         "possible_guesses": possible_guesses,
#     }
#
#     evidence = []
#     while True:
#         if not global_game_state["possible_guesses"]:
#             print("No more possible guesses. Probably an error in your inputs.")
#             break
#         guess = generate_next_guess(global_game_state, evidence)
#         if guess is None:
#             print("Ran out of possible guesses.")
#             break
#         print(f"Next guess: {',  '.join(guess)}")
#         both_correct = int(
#             input("Enter number of correct symbols in correct positions: ")
#         )
#         symbol_correct = int(
#             input("Enter number of correct symbols in wrong positions: ")
#         )
#
#         if both_correct == num_pegs:
#             print("Solved!")
#             break
#
#         evidence.append(
#             {
#                 "guess": guess,
#                 "both_correct": both_correct,
#                 "symbol_correct": symbol_correct,
#             }
#         )


if __name__ == "__main__":
    print("Mansion of Madness Puzzle Solver")
    # symbols = input("Enter symbols (comma-separated): ").split(",")

    symbols = ["r", "y", "g", "b", "o"]
    solver = PuzzleSolver(symbols)

    print(f"Using random seed: {solver.seed}")
    solver.solve()
