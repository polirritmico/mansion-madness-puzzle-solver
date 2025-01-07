#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from solver import PuzzleSolver, Score


@pytest.fixture
def symbols():
    return ("g", "y", "b", "r", "w")


def test_algorithm_implementation_case1() -> None:
    symbols = ["1", "2", "3"]
    answer = ("3", "1", "1")
    seed = 1

    guess_results = ((0, 1), (2, 0), (5, 0))

    solver = PuzzleSolver(symbols, seed=seed)
    output = ()

    for result in guess_results:
        output = solver.search_next_guess()
        solver.register_results(output, Score(*result))

    assert output == answer


def test_algorithm_implementation_case2() -> None:
    symbols = ["1", "2", "3"]
    answer = ("1", "2", "1")
    seed = 1

    guess_results = ((2, 0), (2, 0), (5, 0))

    solver = PuzzleSolver(symbols, seed=seed)
    output = ()

    for result in guess_results:
        output = solver.search_next_guess()
        solver.register_results(output, Score(*result))

    assert output == answer


def test_repeated_symbols_from_input() -> None:
    symbols = ["1", "2", "2", "2", "2"]
    expected_size = 5
    expected_symbols = ["1", "2"]

    solver = PuzzleSolver(symbols)

    assert expected_size == solver.size
    assert expected_symbols == solver.symbols


def test_case_from_playthrough(symbols) -> None:
    expected = ("w", "y", "r", "w", "r")
    seed = 666

    expected_guesses = (
        ("b", "w", "w", "r", "r"),
        ("r", "b", "w", "w", "w"),
        ("y", "r", "b", "r", "w"),
        ("r", "w", "r", "g", "b"),
    )
    register_results = ((1, 3), (1, 2), (0, 4), (1, 2))

    solver = PuzzleSolver(symbols, seed=seed)

    for exp_guess, exp_results in zip(expected_guesses, register_results):
        assert exp_guess == solver.search_next_guess()
        solver.register_results(exp_guess, Score(*exp_results))
        assert not solver.check_for_solved_puzzle()
    output = solver.search_next_guess()

    assert output == expected


def test_case1(symbols) -> None:
    expected = ("b", "b", "g", "b", "w")
    seed = 666

    expected_guesses = (
        ("b", "w", "w", "r", "r"),
        ("y", "w", "y", "b", "y"),
        ("b", "y", "r", "b", "g"),
        ("g", "b", "w", "b", "g"),
    )
    register_results = ((1, 1), (1, 1), (2, 1), (2, 2))

    solver = PuzzleSolver(symbols, seed=seed)

    for exp_guess, exp_results in zip(expected_guesses, register_results):
        assert exp_guess == solver.search_next_guess()
        solver.register_results(exp_guess, Score(*exp_results))
        assert not solver.check_for_solved_puzzle()
    output = solver.search_next_guess()

    assert output == expected


def test_case2(symbols) -> None:
    expected = ("b", "b", "b", "g", "y")
    seed = 666

    expected_guesses = (
        ("b", "w", "w", "r", "r"),
        ("g", "w", "g", "y", "g"),
        ("b", "b", "y", "g", "y"),
    )
    register_results = ((1, 0), (0, 2), (4, 0))

    solver = PuzzleSolver(symbols, seed=seed)

    for exp_guess, exp_results in zip(expected_guesses, register_results):
        assert exp_guess == solver.search_next_guess()
        solver.register_results(exp_guess, Score(*exp_results))
        assert not solver.check_for_solved_puzzle()
    output = solver.search_next_guess()

    assert output == expected


def test_case3(symbols) -> None:
    expected = ("w", "y", "r", "b", "y")
    seed = 666

    expected_guesses = (
        ("b", "w", "w", "r", "r"),
        ("r", "y", "b", "g", "w"),
        ("r", "b", "g", "w", "b"),
        ("g", "r", "r", "y", "w"),
        ("w", "g", "y", "b", "w"),
    )
    register_results = ((0, 3), (1, 3), (0, 3), (1, 2), (2, 1))

    solver = PuzzleSolver(symbols, seed=seed)

    for exp_guess, exp_results in zip(expected_guesses, register_results):
        assert exp_guess == solver.search_next_guess()
        solver.register_results(exp_guess, Score(*exp_results))
        assert not solver.check_for_solved_puzzle()
    output = solver.search_next_guess()

    assert output == expected


def test_case4(symbols) -> None:
    expected = ("b", "b", "r", "b", "g")
    seed = 666

    expected_guesses = (
        ("b", "w", "w", "r", "r"),
        ("y", "w", "y", "b", "y"),
    )
    register_results = ((1, 1), (1, 0))

    solver = PuzzleSolver(symbols, seed=seed)

    for exp_guess, exp_results in zip(expected_guesses, register_results):
        assert exp_guess == solver.search_next_guess()
        solver.register_results(exp_guess, Score(*exp_results))
        assert not solver.check_for_solved_puzzle()
    output = solver.search_next_guess()

    assert output == expected


def test_case5(symbols) -> None:
    expected = ("g", "y", "r", "y", "r")
    seed = 666

    expected_guesses = (
        ("b", "w", "w", "r", "r"),
        ("y", "w", "y", "b", "y"),
        ("g", "g", "b", "y", "r"),
        ("g", "g", "w", "y", "w"),
    )
    register_results = ((1, 1), (0, 2), (3, 0), (2, 0))

    solver = PuzzleSolver(symbols, seed=seed)

    for exp_guess, exp_results in zip(expected_guesses, register_results):
        assert exp_guess == solver.search_next_guess()
        solver.register_results(exp_guess, Score(*exp_results))
        assert not solver.check_for_solved_puzzle()
    output = solver.search_next_guess()

    assert output == expected


def test_case6(symbols) -> None:
    expected = ("r", "g", "r", "r", "b")
    seed = 666

    expected_guesses = (
        ("b", "w", "w", "r", "r"),
        ("g", "w", "r", "y", "w"),
        ("r", "y", "b", "y", "r"),
        ("g", "r", "b", "r", "b"),
    )
    register_results = ((1, 2), (1, 1), (1, 2), (2, 2))

    solver = PuzzleSolver(symbols, seed=seed)

    for exp_guess, exp_results in zip(expected_guesses, register_results):
        assert exp_guess == solver.search_next_guess()
        solver.register_results(exp_guess, Score(*exp_results))
        assert not solver.check_for_solved_puzzle()
    output = solver.search_next_guess()

    assert output == expected
