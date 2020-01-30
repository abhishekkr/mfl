# to provide functionality on creating dataframes for MF data by URL/name
import logging
from datetime import datetime
import pandas as pd
from pandas.io.json import json_normalize
from . import mfapi


def from_url(mf_url):
    mf_json = mfapi.mf_json_from_url(mf_url)
    dataframe = json_normalize(mf_json)
    dataframe['date'] = dataframe['date'].apply(null_date_converter)
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe.set_index('date', inplace=True)
    df_mf = dataframe.astype(float)
    return fill_null(df_mf)


def fill_null(dataframe):
    return dataframe.fillna(dataframe.bfill()) # taking care of null fields


def null_date_converter(value):
    try:
        return datetime.strptime(value, "%d-%m-%Y").date()
    except:
        logging.warning("failed date conversion in dataframe for: %s" % (value))
        return None
