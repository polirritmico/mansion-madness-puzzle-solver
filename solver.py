#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from dataclasses import dataclass
from itertools import product


@dataclass
class Score:
    full_match: int = 0
    partial_match: int = 0


@dataclass
class GuessResults:
    sequence: tuple[str, ...]
    score: Score

    def __repr__(self):
        return str(self.sequence)


class PuzzleSolver:
    symbols: tuple[str, ...]
    size: int
    seed: int
    permutations: list[tuple[str, ...]]
    registers: list[GuessResults]

    def __init__(self, symbols: tuple[str, ...], seed: int = None):
        self.symbols = symbols
        self.size = len(symbols)
        assert self.size > 1

        self.seed = random.randint(0, 99999) if seed is None else seed
        random.seed(self.seed)

        self.permutations: list[tuple[str, ...]] = list(
            product(self.symbols, repeat=self.size)
        )
        self.registers: list[GuessResults] = []

    def next_guess(self) -> tuple[str, ...]:
        while self.permutations:
            selected_random_position = random.randint(0, len(self.permutations) - 1)
            next_guess = self.permutations.pop(selected_random_position)
            if self.guess_respects_registered_entries_data(next_guess):
                return next_guess
        return None

    def guess_respects_registered_entries_data(self, guess: tuple[str, ...]) -> bool:
        for register in self.registers:
            score = self.comparation_score(guess, register.sequence)
            if score.full_match != register.score.full_match:
                return False
            if score.partial_match != register.score.partial_match:
                return False
        return True

    def comparation_score(
        self, current_seq: list[str], reference_seq: list[str]
    ) -> Score:
        full_matches = 0
        partial_matches = 0
        remaning_reference_symbols = []
        remaning_current_symbols = []
        for current_symbol, reference_symbol in zip(current_seq, reference_seq):
            if current_symbol == reference_symbol:
                full_matches += 1
            else:
                remaning_reference_symbols.append(current_symbol)
                remaning_current_symbols.append(reference_symbol)

        for reference_symbol in remaning_reference_symbols:
            if reference_symbol in remaning_current_symbols:
                partial_matches += 1
                remaning_current_symbols.remove(reference_symbol)

        return Score(full_matches, partial_matches)

    def ask_results_to_user(self, guess) -> Score:
        base_msg = "Enter number of correct symbols in {} positions: "
        full_match = int(input(base_msg.format("correct")) or 0)
        if full_match == self.size:
            return Score(full_match, 0)
        partial_match = int(input(base_msg.format("wrong")) or 0)
        return Score(full_match, partial_match)

    def evaluate_guess_results(
        self, guess: tuple[str, ...], score: Score | None = None
    ) -> bool:
        if score is None:
            score = self.ask_results_to_user(guess)

        if score.full_match == self.size:
            return True

        self.registers.append(GuessResults(guess, score))
        return False

    def solve(self) -> None:
        while True:
            guess = self.next_guess()
            if guess is None:
                print("No more possible guesses. Probably an error in your inputs.")
                break
            print(f"Next guess: {',  '.join(guess)}")

            if self.evaluate_guess_results(guess):
                print("Solved!")
                break


if __name__ == "__main__":
    print("Mansion of Madness Puzzle Solver")
    # symbols = input("Enter symbols (comma-separated): ").split(",")

    # Mastermind style
    # symbols = ["r", "y", "g", "b", "o"]
    # solver = PuzzleSolver(symbols)

    # Mansion of Madness style
    symbols = ["g", "y", "b", "r", "w"]
    solver = PuzzleSolver(symbols, 666)

    print(f"Using random seed: {solver.seed}")
    solver.solve()
