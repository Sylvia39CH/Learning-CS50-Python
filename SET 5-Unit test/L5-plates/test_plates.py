from plates import is_valid
import pytest

def main():
    test_onlyalpha()
    test_withnumbers()

def test_onlyalpha():
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAA") == True
    assert is_valid("AAAAAAA") == False


def test_withnumbers():
    assert is_valid("A3") == False
    assert is_valid("AA3A3") == True
    assert is_valid("A33A") == False
    assert is_valid("AA3AA") == False

if __name__ =="__main__":
    main()