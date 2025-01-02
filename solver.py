#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from dataclasses import dataclass
from itertools import product


@dataclass
class CaseRegister:
    symbols: tuple[str, ...]
    full_match: int = 0
    partial_match: int = 0


class PuzzleSolver:
    symbols: tuple[str, ...]
    size: int
    seed: int
    possibilities: list[list[str]]
    register: list[CaseRegister]

    def __init__(self, symbols: tuple[str, ...], seed: int = None):
        self.symbols = symbols
        self.size = len(symbols)
        assert self.size > 1

        self.seed = random.randint(0, 99999) if seed is None else seed
        random.seed(self.seed)

        self.possibilities = list(product(self.symbols, repeat=self.size))
        self.register: list[CaseRegister] = []

    def next_guess(self) -> tuple[str, ...]:
        while self.possibilities:
            next_guess = self.possibilities.pop(
                random.randint(0, len(self.possibilities) - 1)
            )
            if not self.guess_contradicts_register(next_guess):
                return next_guess
        return None

    def guess_contradicts_register(self, guess) -> bool:
        for case in self.register:
            partial_matches, full_matches = self.judge_guess(guess, case.symbols)
            if partial_matches != case.full_match:
                return True
            if full_matches != case.partial_match:
                return True
        return False

    def evaluate_guess_results(
        self, guess, both_good: int | None = None, symbol_good: int | None = None
    ) -> bool:
        base_msg = "Enter number of correct symbols in {} positions: "

        if both_good is None:
            both_good = int(input(base_msg.format("correct")) or 0)

        if both_good == self.size:
            return True

        if symbol_good is None:
            symbol_good = int(input(base_msg.format("wrong")) or 0)

        self.register.append(CaseRegister(guess, both_good, symbol_good))
        return False

    def judge_guess(self, answer: list[str], guess: list[str]) -> tuple[int, int]:
        full_match = 0
        partial_match = 0
        unacounted_answers = []
        unacounted_guesses = []
        for a, g in zip(answer, guess):
            if a == g:
                full_match += 1
            else:
                unacounted_answers.append(a)
                unacounted_guesses.append(g)

        for ua in unacounted_answers:
            if ua in unacounted_guesses:
                partial_match += 1
                unacounted_guesses.remove(ua)

        return (full_match, partial_match)

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
