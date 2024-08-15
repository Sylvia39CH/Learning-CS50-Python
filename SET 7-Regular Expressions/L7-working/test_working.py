import pytest
from working import convert

def test_1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_3():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"

def test_wrong_input_pattern():
    with pytest.raises(ValueError):
        assert convert("9 AM - 5 PM")
        assert convert("9 AM to 5 ")

def test_wrong_time_pattern():
    with pytest.raises(ValueError):
        assert convert("9:60 AM to 5 PM")
        assert convert("0 AM to 5 PM")