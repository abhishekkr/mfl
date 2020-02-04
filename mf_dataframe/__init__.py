# to provide functionality on creating dataframes for MF data by URL/name
import pandas as pd
from pandas.io.json import json_normalize
import statsmodels.api as sm

from . import mod
import mf_data

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


def from_url(mf_url):
    mf_json = mf_data.json_from_url(mf_url)
    dataframe = json_normalize(mf_json)
    dataframe['date'] = dataframe['date'].apply(mod.null_date_converter)
    dataframe['date'] = pd.to_datetime(dataframe['date'])
    dataframe.set_index('date', inplace=True)
    df_mf = dataframe.astype(float)
    return mod.fill_null(df_mf)


def plot(dataframe):
    dataframe.plot(figsize=(15, 6))
    plt.show()


def plot_seasonal_decompose(dataframe):
    decomposition = sm.tsa.seasonal_decompose(dataframe, model='additive')
    fig = decomposition.plot()
    plt.show()


def info(dataframe):
    print([dataframe.max()])
    print([dataframe.min()])
    print(dataframe.dtypes)
    print(dataframe.info())
    print(dataframe.isnull().sum())
    print(dataframe.head())
    print(dataframe.index)
    print(dataframe.head(3))
