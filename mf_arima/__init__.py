#
import statsmodels.api as sm

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


def fit_model(dataframe):
    arima_model = sm.tsa.statespace.SARIMAX(
        dataframe,
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, 12),
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    return arima_model.fit()


def plot_diagnostics(arima_model):
    print(arima_model.summary().tables[1])
    arima_model.plot_diagnostics(figsize=(15, 12))
    plt.show()
