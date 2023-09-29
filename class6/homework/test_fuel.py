from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("1/4") ==25

def test_converterror():
    with pytest.raises(ValueError):
        convert("cat/3")
    with pytest.raises(ValueError):
        convert("4/3")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_gauge():
    assert gauge(25) =="25%"
    assert gauge(99) =="F"
    assert gauge(1) =="E"