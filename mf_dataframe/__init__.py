# to provide functionality on creating dataframes for MF data by URL/name
import pandas as pd
from pandas.io.json import json_normalize
from . import mfapi, mod


def from_url(mf_url):
    mf_json = mfapi.mf_json_from_url(mf_url)
    dataframe = json_normalize(mf_json)
    dataframe['date'] = dataframe['date'].apply(mod.null_date_converter)
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe.set_index('date', inplace=True)
    df_mf = dataframe.astype(float)
    return mod.fill_null(df_mf)
