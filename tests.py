#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import main
from main import PuzzleSolver


@pytest.fixture
def symbols():
    return ["r", "y", "g", "b", "o"]


def test_case1(symbols) -> None:
    case = ["g", "b", "g", "b", "y"]
    seed = 3795
    expected = "g, b, g, b, y"

    solver = PuzzleSolver(symbols, seed)

    guess = ["g", "g", "y", "r", "b"]
    correct_pos_and_symbol = 1
    correct_symbols = 3
    guess = ["g", "o", "r", "b", "y"]
    correct_pos_and_symbol = 3
    correct_symbols = 0
    guess = ["g", "b", "r", "b", "g"]
    correct_pos_and_symbol = 3
    correct_symbols = 1
    guess = ["g", "b", "g", "b", "y"]
    correct_pos_and_symbol = 5
    correct_symbols = 0


def test_case2() -> None:
    case = ["o", "r", "g", "g", "o"]
    seed = 16

    guess = ["g", "y", "o", "y", "r"]
    correct_pos_and_symbol = 0
    correct_symbols = 3
    guess = ["y", "g", "g", "r", "b"]
    correct_pos_and_symbol = 1
    correct_symbols = 2
    guess = ["o", "o", "g", "b", "y"]
    correct_pos_and_symbol = 2
    correct_symbols = 1
    guess = ["r", "o", "y", "b", "b"]
    correct_pos_and_symbol = 0
    correct_symbols = 2
    guess = ["o", "r", "g", "g", "o"]
    correct_pos_and_symbol = 5
    correct_symbols = 0


def test_case3() -> None:
    case = ["y", "y", "y", "y", "g"]
    seed = 7226

    guess = ["r", "y", "y", "b", "o"]
    correct_pos_and_symbol = 2
    correct_symbols = 0
    guess = ["g", "y", "o", "o", "o"]
    correct_pos_and_symbol = 1
    correct_symbols = 1
    guess = ["b", "y", "b", "b", "g"]
    correct_pos_and_symbol = 2
    correct_symbols = 0
    guess = ["y", "y", "y", "y", "g"]
    correct_pos_and_symbol = 5
    correct_symbols = 0


def test_case4() -> None:
    guess = ["o", "b", "y", "o", "g"]
    seed = 9718

    guess = ["r", "o", "o", "g", "b"]
    correct_pos_and_symbol = 0
    correct_symbols = 4
    guess = ["y", "r", "g", "o", "o"]
    correct_pos_and_symbol = 1
    correct_symbols = 3
    guess = ["o", "r", "b", "y", "g"]
    correct_pos_and_symbol = 2
    correct_symbols = 2
    guess = ["o", "y", "b", "r", "o"]
    correct_pos_and_symbol = 1
    correct_symbols = 3
    guess = ["o", "b", "y", "o", "g"]
    correct_pos_and_symbol = 5
    correct_symbols = 0


def test_case5() -> None:
    case = ["r", "r", "r", "r", "b"]
    seed = 1001

    guess = ["r", "y", "o", "b", "r"]
    correct_pos_and_symbol = 1
    correct_symbols = 2
    guess = ["b", "b", "o", "r", "b"]
    correct_pos_and_symbol = 2
    correct_symbols = 0
    guess = ["r", "b", "r", "r", "g"]
    correct_pos_and_symbol = 3
    correct_symbols = 1
    guess = ["r", "r", "r", "r", "b"]
    correct_pos_and_symbol = 5
    correct_symbols = 0
