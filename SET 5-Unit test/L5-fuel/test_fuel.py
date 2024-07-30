from fuel import convert,gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/2") == 0.5
    with pytest.raises(SystemExit):
        assert convert("2/1")

def test_zero_division():
    with pytest.raises(SystemExit):
        assert convert("2/0")

def test_value():
    with pytest.raises(SystemExit):
        assert convert("a/b")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "F"
    assert gauge(0.5) == "50%"



if __name__ =="__main__":
    main()