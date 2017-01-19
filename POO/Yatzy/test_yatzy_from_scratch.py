import pytest
from yatzy import Yatzy

# Chance
# The player scores the sum of all dice, no matter what they read.


def test_chance():
    # iterar sobre *args evita codigo cableado a 5 argumentos
    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)


def test_twos():
    assert 4 == Yatzy.twos(2, 3, 2, 5, 1)
    assert 2 == Yatzy.twos(1, 1, 2, 4, 4)
    assert 0 == Yatzy.twos(3, 3, 3, 4, 5)

def test_pair():
    assert 8 == Yatzy.pair(3,3,3,4,4)
    assert 12 == Yatzy.pair(1,1,6,2,6)
    assert 6 == Yatzy.pair(3,3,3,4,1)
    assert 6 == Yatzy.pair(3,3,3,3,1)
    assert 4 == Yatzy.pair(2,2,2,2,2)
    assert 0 == Yatzy.pair(1,2,3,4,5)

def test_two_pair():
    assert 8 == Yatzy.two_pair(1,1,2,3,3)
    assert 0 == Yatzy.two_pair(1,1,2,3,4)
    assert 6 == Yatzy.two_pair(1,1,2,2,2)
    assert 8 == Yatzy.two_pair(2,2,2,2,2)