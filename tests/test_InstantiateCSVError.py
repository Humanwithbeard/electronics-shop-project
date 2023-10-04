import pytest

from src.InstantiateCSVError import InstantiateCSVError

@pytest.fixture()
def instance_csv_error():
    return InstantiateCSVError

def test_instantiates_csv_error(instance_csv_error):
    with pytest.raises(FileNotFoundError):
        open('../src/item.csv')
