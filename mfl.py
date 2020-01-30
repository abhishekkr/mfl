#!python3
"""
to predict Mutual Fund NAV
reference:
    * https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-visualization-with-python-3
    * https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3
    * https://towardsdatascience.com/an-end-to-end-project-on-time-series-analysis-and-forecasting-with-python-4835e6bf050b
"""

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

import warnings
warnings.filterwarnings("ignore")

from pylab import rcParams
import matplotlib
matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'
matplotlib.rcParams['figure.figsize'] = 11, 9

import mf_arima
import mf_dataframe
from mf_dataframe import resample as mf_dataframe_resample


### constants
sbi_direct_growth = {
    'technologies opportunities fund': 'https://api.mfapi.in/mf/120578',
    'contra fund': 'https://api.mfapi.in/mf/119835'
}


### helper

def showtime(dataframe):
    mf_dataframe.info(dataframe)
    mf_dataframe.plot(dataframe)
    mf_dataframe.plot_seasonal_decompose(dataframe)

    arima_model = mf_arima.fit_model(dataframe)
    mf_arima.plot_diagnostics(arima_model)

    mf_arima.validate(dataframe, arima_model, '2015-01-01', '2018-01-01')
    mf_arima.validate(dataframe[:'2020-01-01'], arima_model, '2015', '2019-01-01')
    mf_arima.predict(dataframe, arima_model, 50)


### main

if __name__ == '__main__':
    df_nav = mf_dataframe.from_url(sbi_direct_growth['technologies opportunities fund'])

    df_navmonthly = mf_dataframe_resample.monthly_sample_dataframe(df_nav)
    df_navweekly = mf_dataframe_resample.monthly_sample_dataframe(df_nav)
    df_bizday = mf_dataframe_resample.bizday_sample_dataframe(df_nav)
    df_day = mf_dataframe_resample.day_sample_dataframe(df_nav)

    showtime(df_navweekly)
