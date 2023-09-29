from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") ==0
    assert value("    hello") ==0
    
def test_h():
    assert value("hey")==20
    assert value("how are you?") ==20

def test_other():
    assert value("0") ==100
    assert value("What's up") ==100