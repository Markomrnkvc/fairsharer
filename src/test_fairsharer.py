from fairsharer.py import fair_sharer
import pytest

def test_fair_sharer():
    assert fair_sharer([0,1000,800,0], 1) == [100, 800, 900, 0]
    assert fair_sharer([0, 1000, 800, 0], 2) == [100, 890, 720, 90]
