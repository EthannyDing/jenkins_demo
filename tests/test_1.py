"""."""
import pytest
import pandas as pd


@pytest.fixture(scope='module')
def test_df():
    f = pd.read_csv('tests/test.csv')
    return f


@pytest.mark.incremental
def test_get_mortality(test_df):

    assert len(test_df.columns) == 2, 'number of columns is not 2'

