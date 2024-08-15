import pytest
from um import count

def test_yummy():
    assert count("Ummm, this is, um, yummy!") == 1
    assert count("This is, um, yummy!") == 1
    assert count("Ummm, um, this is, um, yummy!") == 2
    assert count("Ummm, this is yummy!") == 0

def test_upper():
    assert count("Um, this is, um, yummy!") == 2
    assert count("Um, um, um, this is, um, yummy!") == 4

def test_char():
    assert count("Um?? this is, um?..yummy!") == 2
    assert count("This is.......um, yummy!") == 1
