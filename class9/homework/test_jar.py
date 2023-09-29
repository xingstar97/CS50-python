from jar import Jar
import pytest

def test_init():
    assert Jar(12).capacity ==12
    with pytest.raises(ValueError):
        Jar("Cat")
    with pytest.raises(ValueError):
        Jar(-2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(12)
    assert jar.deposit(1) == 1
    assert jar.deposit(3) ==4
    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar(12)
    jar.deposit(12)
    assert jar.withdraw(1) ==11
    assert jar.withdraw(11) == 0
    with pytest.raises(ValueError):
        jar.withdraw(21)