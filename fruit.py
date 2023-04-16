import pytest


class Fruit:
    def __init__(self, name, units_available, color, price):
        self.name = name
        self.units_available = units_available
        self.color = color
        self.price = price

    def request(self, number_of_units):
        text = "I'd like {0} {1} {2}s"
        return text.format(number_of_units, self.color, self.name)

    def pick_amount(self, number_of_units):
        return number_of_units if number_of_units < self.units_available else self.units_available

    def calculate_price(self, number_of_units):
        return number_of_units * self.price


# tests in pytest can be in the class file itself
def test_request():  # method name must start with "test_"
    plum = Fruit('plum', 16, 'purple', 2)
    request = plum.request(4)
    assert "I'd like 4 purple plums" == request


# fixture works as a setup method, and runs once, staying in cache
@pytest.fixture
def plum():
    return Fruit('plum', 16, 'purple', 2)


def test_request_with_fixture(plum):
    request = plum.request(4)
    assert "I'd like 4 purple plums" == request
