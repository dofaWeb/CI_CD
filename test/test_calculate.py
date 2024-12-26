from .. import calculate 
def test_add():
    a = 1
    b = 1
    assert calculate.add(a, b) == 2
    assert calculate.add(1, 2) == 3
    assert calculate.add(1, 2) == 4