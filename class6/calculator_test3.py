from calculator6 import square

def test_calculator():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) ==9
    assert square (0) == 0

#pytest calculator_test3.py