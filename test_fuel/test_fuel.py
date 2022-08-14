from fuel import convert, gauge
import pytest

def main():
    test_convert()
    test_gauge()

def test_convert():
    assert convert("1/4") == 25
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1.5/4")
    with pytest.raises(ValueError):
        convert("8/4")
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_gauge():
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(99) == "F"

if __name__ == "__main__":
    main()