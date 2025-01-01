#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from solver import PuzzleSolver


@pytest.fixture
def symbols():
    return ["r", "y", "g", "b", "o"]


def test_case1(symbols) -> None:
    expected = ["g", "b", "b", "g", "r"]
    seed = 31638

    expected_guesses = [
        ["r", "r", "y", "r", "o"],
        ["b", "g", "r", "b", "b"],
    ]
    register_results = [(0, 1), (0, 4)]

    solver = PuzzleSolver(symbols, seed)

    for exp_guess, exp_results in zip(expected_guesses, register_results):
        assert exp_guess == solver.next_guess()
        assert not solver.evaluate_guess_results(exp_guess, *exp_results)
    output = solver.next_guess()

    assert output == expected


def test_case2(symbols) -> None:
    expected = ["b", "r", "o", "y", "y"]
    seed = 76917

    expected_guesses = [
        ["o", "b", "b", "r", "r"],
        ["r", "o", "r", "y", "g"],
        ["g", "y", "r", "b", "b"],
        ["b", "r", "g", "o", "g"],
    ]
    register_results = [(0, 3), (1, 2), (0, 3), (2, 1)]

    solver = PuzzleSolver(symbols, seed)

    for exp_guess, exp_results in zip(expected_guesses, register_results):
        assert exp_guess == solver.next_guess()
        assert not solver.evaluate_guess_results(exp_guess, *exp_results)
    output = solver.next_guess()

    assert output == expected


def test_case3(symbols) -> None:
    expected = ["g", "y", "y", "r", "g"]
    seed = 17284

    expected_guesses = [
        ["y", "g", "r", "b", "r"],
        ["b", "b", "y", "r", "b"],
        ["g", "y", "y", "g", "b"],
        ["g", "b", "y", "g", "g"],
    ]
    register_results = [(0, 3), (2, 0), (3, 1), (3, 0)]

    solver = PuzzleSolver(symbols, seed)

    for exp_guess, exp_results in zip(expected_guesses, register_results):
        assert exp_guess == solver.next_guess()
        assert not solver.evaluate_guess_results(exp_guess, *exp_results)
    output = solver.next_guess()

    assert output == expected
