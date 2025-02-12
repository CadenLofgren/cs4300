def add_int(x):
    temp = x + 1
    return temp


def add_floating(x):
    temp = x + 2.39
    temp = round(temp, 2)
    return temp


def hello(name):
    say_hello = f"Hello {name}"
    return say_hello


def is_positive(x):
    is_pos = x > 0
    return is_pos


def test_add_int():
    assert add_int(1) == 2


def test_add_floating():
    assert add_floating(2) == 4.39


def test_hello():
    assert hello("Caden") == "Hello Caden"


def test_is_positive():
    assert is_positive(1) == True