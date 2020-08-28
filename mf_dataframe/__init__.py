# to provide functionality on creating dataframes for MF data by URL/name
import pandas as pd
from pandas.io.json import json_normalize
import statsmodels.api as sm

from . import mod
from . import resample as mf_dataframe_resample
import mf_data
import mf_arima

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


def showtime(dataframe):
    info(dataframe)
    plot(dataframe)
    plot_seasonal_decompose(dataframe)

    arima_model = mf_arima.fit_model(dataframe)
    mf_arima.plot_diagnostics(arima_model)

    mf_arima.validate(dataframe, arima_model, '2015-01-01', '2018-01-01')
    mf_arima.validate(dataframe[:'2020-01-01'], arima_model, '2015', '2019-01-01')
    mf_arima.predict(dataframe, arima_model, 50)


def showtime_from_mfapi_in(fund_name):
    df_nav = from_url(mf_data.api_from_mfapi_in(fund_name))

    df_navmonthly = mf_dataframe_resample.monthly_sample_dataframe(df_nav)
    df_navweekly = mf_dataframe_resample.monthly_sample_dataframe(df_nav)
    df_bizday = mf_dataframe_resample.bizday_sample_dataframe(df_nav)
    df_day = mf_dataframe_resample.day_sample_dataframe(df_nav)

    showtime(df_navweekly)
