from calculadora import somar


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-2, 2) == 0
    assert somar(1.5, 2.5) == 4
