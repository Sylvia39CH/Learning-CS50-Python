from bank import value

def main():
    test_value()

def test_value():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("dude") == 100

if __name__ =="__main__":
    main()