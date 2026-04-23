# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
from arana.rndm import RandomInt


def test_value() -> None:
    start = 0
    end = 10
    random_int = RandomInt()
    value = random_int.value(start, end)
    assert value >= start
    assert value <= end


def test_values() -> None:
    random_int = RandomInt()
    values = random_int.values(1, 10)
    assert sorted(values) == sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def test_values_length_1() -> None:
    random_int = RandomInt()
    values = random_int.values(1, 1)
    assert len(values) == 1


def test_values_length_10() -> None:
    size = 10
    random_int = RandomInt()
    values = random_int.values(1, 10)
    assert len(values) == size
