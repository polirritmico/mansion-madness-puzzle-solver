#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from dataclasses import dataclass
from itertools import product


@dataclass
class Score:
    full_match: int = 0
    partial_match: int = 0

    def __repr__(self):
        return f"({self.full_match}, {self.partial_match})"


@dataclass
class GuessResults:
    sequence: tuple[str, ...]
    score: Score

    def __repr__(self):
        return str(self.sequence)


class PuzzleSolver:
    symbols: tuple[str, ...]
    size: int
    permutations: list[tuple[str, ...]]
    registers: list[GuessResults]

    def __init__(
        self, symbols: list[str], seed: int | None = None, size: int | None = None
    ):
        self.size = len(symbols) if size is None else size
        self.symbols = self.remove_duplicated_symbols(symbols)
        assert self.size > 1
        assert len(symbols) > 1

        if seed is None:
            seed = random.randint(0, 99999)
            print(f"Using '{seed}' as the chaos seed")
        random.seed(seed)

        self.permutations: list[tuple[str, ...]] = list(
            product(self.symbols, repeat=self.size)
        )
        self.registers: list[GuessResults] = []
        self.iteration_counter = 0

    def remove_duplicated_symbols(self, symbols: list[str]) -> list[str]:
        return list(dict.fromkeys(symbols))

    def search_next_guess(self) -> tuple[str, ...]:
        while self.permutations:
            selected_random_position = random.randint(0, len(self.permutations) - 1)
            next_guess = self.permutations.pop(selected_random_position)
            if self.validate_againts_all_register_entries(next_guess):
                return next_guess
        return None

    def validate_againts_all_register_entries(self, guess: tuple[str, ...]) -> bool:
        """
        Returns `True` if the `guess` matches the same score for both full and partial
        matches as every entry in the register, ensuring the guess is one of the valid
        possible answers. (The larger the register, the more it narrows down the set of
        potential correct answers)
        """
        for register in self.registers:
            self.iteration_counter += 1

            score = self.score_matching_symbols(guess, register.sequence)
            if score.full_match != register.score.full_match:
                return False
            if score.partial_match != register.score.partial_match:
                return False
        return True

    def score_matching_symbols(self, guess: list[str], register: list[str]) -> Score:
        full_match_score = 0
        partial_match_score = 0

        unpaired_guess_symbols = []
        unpaired_register_symbols = []

        for guess_symbol, register_symbol in zip(guess, register):
            if guess_symbol == register_symbol:
                full_match_score += 1
            else:
                unpaired_guess_symbols.append(guess_symbol)
                unpaired_register_symbols.append(register_symbol)

        for guess_symbol in unpaired_guess_symbols:
            if guess_symbol in unpaired_register_symbols:
                partial_match_score += 1
                unpaired_register_symbols.remove(guess_symbol)

        return Score(full_match_score, partial_match_score)

    def ask_results_to_user(self) -> Score:
        base_msg = "Enter number of correct symbols in {} positions: \n"
        full_match = int(input(base_msg.format("correct")) or 0)
        if full_match == self.size:
            return Score(full_match, 0)
        partial_match = int(input(base_msg.format("wrong")) or 0)
        return Score(full_match, partial_match)

    def register_results(self, guess: tuple[str, ...], score: Score | None = None):
        if score is None:
            score = self.ask_results_to_user()

        self.registers.append(GuessResults(guess, score))

    def check_for_solved_puzzle(self) -> bool:
        last_register = self.registers[-1]
        return last_register.score.full_match == self.size

    def print_guess(self, sequence: tuple[str, ...]) -> None:
        color_map = {
            "o": "\033[1m\033[38;5;214m",  # ]] Orange
            "r": "\033[1m\033[31m",  # ]] Red
            "y": "\033[1m\033[93m",  # ]] Yellow
            "g": "\033[1m\033[32m",  # ]] Green
            "b": "\033[1m\033[96m",  # ]] Blue (light)
            "w": "\033[1m\033[97m",  # ]]Grey (light)
            "_": "\033[0m",  # ]] No style/reset
        }
        res = []
        for symbol in sequence:
            if symbol in color_map:
                symbol = f"{color_map[symbol]}{symbol.upper()}{color_map['_']}"
            res.append(symbol)

        print("Next guess: " + ", ".join(res))

    def solve(self) -> None:
        print("Solving the puzzle... (Try each guess and insert the results)\n")
        while True:
            guess = self.search_next_guess()
            if guess is None:
                print("No more possible guesses. Probably an error in your inputs.")
                break
            self.print_guess(guess)

            self.register_results(guess)

            if self.check_for_solved_puzzle():
                print("Solved!")
                break


def main():
    def user_input(msg, default, cast_fn=int) -> any:
        raw_input = input(f"{msg} (default '{str(default)}'): ").replace(" ", "")
        return cast_fn(raw_input if raw_input else default)

    def symbols_parser(raw: str) -> list[str]:
        assert isinstance(raw, str)
        return raw.split(",")

    print("🪦 [Mansion of Madness Puzzle Solver] 📚🔯")
    print("------------------------------------------")

    seed = user_input("Enter the chaos seed value", 666)
    size = user_input("Enter the puzzle size value", 5)
    symbols = user_input(
        "Enter the symbols list (comma-separated)", "g,y,b,r,w", symbols_parser
    )

    print("------------------------------------------")

    solver = PuzzleSolver(symbols, seed, size)
    solver.solve()

    # Mastermind style
    # symbols = ["r", "y", "g", "b", "o"]
    # solver = PuzzleSolver(symbols)
    # solver.solver()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Program interrupted by the user.")
    except Exception as e:
        print(f"An error occurred: {type(e).__name__}")
    finally:
        print("Closing...")
