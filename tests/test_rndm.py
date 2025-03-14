# The MIT License (MIT)
#
# Copyright (C) 2025 Fabrício Barros Cabral
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
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
