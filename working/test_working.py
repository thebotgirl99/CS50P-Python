from working import convert
import pytest

def main():
    test_convert()

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 AM to 5 PM") == "00:00 to 17:00"
    assert convert("9 PM to 12 AM") == "21:00 to 00:00"
    assert convert("12:45 AM to 6:30 PM") == "00:45 to 18:30"
    assert convert("6:30 PM to 12:30 AM") == "18:30 to 00:30"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("12:60 AM - 13:00 PM")


if __name__ == "__main__":
    main()