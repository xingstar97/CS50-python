from hello import hello

def test_hello():
    assert hello("Ting") == "hello, Ting"
# WRONG: hello function does not have return value