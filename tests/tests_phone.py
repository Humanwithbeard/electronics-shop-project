import pytest

from src.phone import Phone


@pytest.fixture
def instance_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(instance_phone):
    assert instance_phone.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(instance_phone):
    assert instance_phone.number_of_sim == 2
    with pytest.raises(ValueError):
        instance_phone.number_of_sim = 0


def test_str(instance_phone):
    assert instance_phone.__str__() == 'iPhone 14'