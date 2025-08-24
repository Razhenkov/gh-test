from src.app import calculate

def test_calculate():
    assert calculate(5, 10) == 15
    assert calculate(-1, 1) == 0
    assert calculate(0, 0) == 0