#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


class PuzzleSolver:
    symbols: list[str]
    size: int

    def __init__(self, symbols: list[str], seed: int = None):
        random.seed(seed if seed is not None else random.randint(0, 99999))
        self.symbols = symbols
        self.size = len(symbols)


def pick_from_array(arr):
    return random.choice(arr)


def generate_all_possible_guesses(num_pegs, symbols):
    assert num_pegs >= 1

    if num_pegs == 1:
        return [[symbol] for symbol in symbols]

    suffixes = generate_all_possible_guesses(num_pegs - 1, symbols)
    return [[symbol] + suffix for symbol in symbols for suffix in suffixes]


def judge_guess(answer, guess):
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


def guess_contradicts_some_evidence(guess, evidences):
    for evidence in evidences:
        judgment = judge_guess(guess, evidence["guess"])
        if judgment != {
            "both_correct": evidence["both_correct"],
            "symbol_correct": evidence["symbol_correct"],
        }:
            return True
    return False


def quick_remove_from_array(index, array):
    if index < 0 or index >= len(array):
        raise IndexError("index out of rrange")
    return array.pop(index)


def generate_next_guess(game_state, evidence):
    while game_state["possible_guesses"]:
        guess = quick_remove_from_array(
            random.randint(0, len(game_state["possible_guesses"]) - 1),
            game_state["possible_guesses"],
        )
        if not guess_contradicts_some_evidence(guess, evidence):
            return guess
    return None


def main():
    print("Mansion of Madness Puzzle Solver")
    # num_pegs = int(input("Number of symbols?: "))
    # symbols = input("Enter symbols (comma-separated): ").split(",")
    seed = random.randint(0, 9999)
    random.seed(seed)
    print(f"Using random seed: {seed}")
    num_pegs = 5
    # symbols = "1, 2, 3, 4, 5"
    symbols = "r, y, g, b, o".split(",")

    possible_guesses = generate_all_possible_guesses(num_pegs, symbols)
    global global_game_state
    global_game_state = {
        "num_pegs": num_pegs,
        "symbols": symbols,
        "possible_guesses": possible_guesses,
    }

    evidence = []
    while True:
        if not global_game_state["possible_guesses"]:
            print("No more possible guesses. Probably an error in your inputs.")
            break
        guess = generate_next_guess(global_game_state, evidence)
        if guess is None:
            print("Ran out of possible guesses.")
            break
        print(f"Next guess: {',  '.join(guess)}")
        both_correct = int(
            input("Enter number of correct symbols in correct positions: ")
        )
        symbol_correct = int(
            input("Enter number of correct symbols in wrong positions: ")
        )

        if both_correct == num_pegs:
            print("Solved!")
            break

        evidence.append(
            {
                "guess": guess,
                "both_correct": both_correct,
                "symbol_correct": symbol_correct,
            }
        )


if __name__ == "__main__":
    main()
