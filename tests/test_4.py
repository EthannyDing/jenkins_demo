"""."""
import pytest
import pandas as pd


@pytest.fixture(scope='module')
def test_df():
    f = pd.read_csv('tests/test.csv')
    return f


def test_get_mortality(test_df):

    assert test_df.shape[0] == 3, 'number of rows is not 3'
    assert test_df.shape[1] == 2, 'number of columns is not 2'
    assert sum(test_df.shape) == 5, 'number of columns + row is not 5'
