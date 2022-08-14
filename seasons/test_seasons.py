from seasons import get_mins
import pytest

def main():
    test_get_mins()

def test_get_mins():
    with pytest.raises(SystemExit):
        get_mins("January 1, 1999")
    with pytest.raises(SystemExit):
        get_mins("2, February, 2013")
    with pytest.raises(SystemExit):
        get_mins("1999/12/03")
    with pytest.raises(SystemExit):
        get_mins("1999-January-02")
    with pytest.raises(SystemExit):
        get_mins("2012-31-12")
    assert get_mins("2021-07-28") == "Five hundred twenty-five thousand, six hundred minutes"
    assert get_mins("2020-07-28") == "One million, fifty-one thousand, two hundred minutes"
    assert get_mins("1999-06-09") == "Twelve million, one hundred sixty-eight thousand minutes"

if __name__ == "__main__":
    main()