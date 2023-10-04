import pytest

from src.keyboard import Keyboard


@pytest.fixture
def instance_keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_language(instance_keyboard):
    assert str(instance_keyboard.language) == 'EN'
    instance_keyboard.language = 'RU'
    assert str(instance_keyboard.language) == 'RU'
    with pytest.raises(AttributeError):
        instance_keyboard.language = 'CH'


def test_change_lang(instance_keyboard):
    instance_keyboard.change_lang()
    assert str(instance_keyboard.language) == 'RU'
