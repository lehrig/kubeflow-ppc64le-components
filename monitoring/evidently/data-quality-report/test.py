from typing import Any, Dict, List, Optional, Text
import pandas as pd


'''Try to load data from a cvs file or a json object'''
def _try_load_data(data: Any) -> pd.DataFrame:
    if isinstance(data, str):
        if data.endswith('.csv'):
            return pd.read_csv(data)
        else:
            return pd.read_json(data)
    elif isinstance(data, pd.DataFrame):
        return data
    else:
        raise ValueError('Data should be a path to a csv file or a json object')

# def _try_load_data(data: Any) -> pd.DataFrame:

    