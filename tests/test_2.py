"""."""
import pytest
import pandas as pd


@pytest.fixture(scope='module')
def test_df():
    f = pd.read_csv('tests/test.csv')
    return f


def test_get_mortality(test_df):

    assert test_df.s.sum() == 6, 'column s sum is not 6'

