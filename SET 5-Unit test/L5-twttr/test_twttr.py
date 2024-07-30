from twttr import shorten

def test_shorten():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"

def test_upper():
    assert shorten("HEllO") == "hll"
    assert shorten("tWItter") == "twttr"

def test_char():
    assert shorten("H!!Ell!O") == "h!!ll!"
    assert shorten("t@i@r") == "t@@r"