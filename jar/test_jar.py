from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(9)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(4)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar.deposit(15)
    with pytest.raises(ValueError):
        jar.withdraw(15)

def test_deposit():
    jar = Jar(11)
    jar.deposit(5)
    assert jar.size == 5
    jar = Jar(12,9)
    with pytest.raises(ValueError):
        jar.deposit(5)

def test_withdraw():
    jar = Jar(12)
    jar.deposit(9)
    jar.withdraw(4)
    assert jar.size == 5
    jar = Jar(12,9)
    with pytest.raises(ValueError):
        jar.withdraw(13)

def test_capacity():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(11)
    assert jar.capacity == 11
    with pytest.raises(ValueError):
        jar = Jar(-3)
    with pytest.raises(ValueError):
        jar = Jar("hello")

def test_size():
    jar = Jar()
    assert jar.size == 0
    jar = Jar(11,2)
    assert jar.size == 2
    with pytest.raises(ValueError):
        jar = Jar(12, -3)