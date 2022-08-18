"""."""
import pytest
import pandas as pd


@pytest.fixture(scope='module')
def test_df():
    f = pd.read_csv('tests/test.csv')
    return f


def test_get_mortality(test_df):

    assert test_df.shape[0] == 3, 'number of rows is not 3'
