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

    def comparation_score(self, current: list[str], reference: list[str]) -> Score:
        full_matches = 0
        partial_matches = 0
        reference_symbols_in_wrong_position = []
        current_symbols_in_wrong_position = []

        for current_symbol, reference_symbol in zip(current, reference):
            if current_symbol == reference_symbol:
                full_matches += 1
            else:
                reference_symbols_in_wrong_position.append(reference_symbol)
                current_symbols_in_wrong_position.append(current_symbol)

        for current_symbol in current_symbols_in_wrong_position:
            if current_symbol in reference_symbols_in_wrong_position:
                partial_matches += 1
                reference_symbols_in_wrong_position.remove(current_symbol)

        return Score(full_matches, partial_matches)

    def ask_results_to_user(self) -> Score:
        base_msg = "Enter number of correct symbols in {} positions: "
        full_match = int(input(base_msg.format("correct")) or 0)
        if full_match == self.size:
            return Score(full_match, 0)
        partial_match = int(input(base_msg.format("wrong")) or 0)
        return Score(full_match, partial_match)

    def register_results(self, guess: tuple[str, ...], score: Score | None = None):
        if score is None:
            score = self.ask_results_to_user()

        self.registers.append(GuessResults(guess, score))

    def check_last_guess_solution(self) -> bool:
        last_register = self.registers[-1]
        return last_register.score.full_match == self.size

    def solve(self) -> None:
        while True:
            guess = self.next_guess()
            if guess is None:
                print("No more possible guesses. Probably an error in your inputs.")
                break
            print(f"Next guess: {',  '.join(guess)}")

            self.register_results(guess)

            puzzle_is_solved = self.check_last_guess_solution()
            if puzzle_is_solved:
                print("Solved!")
                break


if __name__ == "__main__":
    print("Mansion of Madness Puzzle Solver")

    # Mastermind style
    # symbols = ["r", "y", "g", "b", "o"]
    # solver = PuzzleSolver(symbols)

    # Mansion of Madness style
    symbols = ["g", "y", "b", "r", "w"]
    solver = PuzzleSolver(symbols, 666)

    print(f"Using random seed: {solver.seed}")
    solver.solve()
