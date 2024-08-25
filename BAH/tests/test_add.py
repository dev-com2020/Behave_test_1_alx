from BAH.my_module import add, multiply, odejmowanie


def test_add():
    """
    Przypadek testowy dla dokumentacji funkcji add()
    :return:
    """
    assert add(2, 3) == 5
    assert add(-2, 5) == 3


def test_multi():
    """
    Przypadek testowy dla dokumentacji funkcji multiply()
    :return:
    """
    assert multiply(2, 2) == 4



def test_odejmowanie():
    """
    Przypadek testowy dla dokumentacji funkcji odejmowanie()
    :return:
    """
    assert odejmowanie(10, 5) == 5
