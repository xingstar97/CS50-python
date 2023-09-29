from calculator6 import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) ==9

def test_zero():
    assert square (0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("Cat")

#TypeError: cat can not be squared
#test if square("cat") indeed will raise TypeError
#with raises TypeError when square("cat")