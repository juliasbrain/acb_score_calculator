import pytest
import pandas as pd
from src.acb_score_calculator import acb_score

def test_acb_score():
    test_df = pd.DataFrame({
        'Subject_ID': ['001', '002'],
        'Med1': ['DrugA: 10mg', 'DrugB: 5mg'],
        'Med2': ['DrugC: 20mg', None]
    })
    result_df = acb_score(test_df)
    assert result_df['acb_score_total'].iloc[0] > 0
