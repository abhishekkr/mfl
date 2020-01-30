#
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


def validate(dataframe, model, start_data_time, start_predict_time):
    pred_dynamic = model.get_prediction(
        start=pd.to_datetime(start_predict_time),
        dynamic=True,
        full_results=True
    )
    pred_dynamic_ci = pred_dynamic.conf_int()
    ax = dataframe[start_data_time:].plot(label='observed', figsize=(20, 15))
    pred_dynamic.predicted_mean.plot(label='forecast', ax=ax)

    ax.fill_between(pred_dynamic_ci.index,
                    pred_dynamic_ci.iloc[:, 0],
                    pred_dynamic_ci.iloc[:, 1], color='k', alpha=.25)
    ax.fill_betweenx(ax.get_ylim(), pd.to_datetime(start_predict_time),
                     dataframe.index[-1], alpha=.1, zorder=-1)

    ax.set_xlabel('Date')
    ax.set_ylabel('NAV Levels')
    plt.legend()
    plt.show()

    y_forecasted = pred_dynamic.predicted_mean
    y_truth = dataframe[start_predict_time:]
    mse = ((y_forecasted - y_truth) ** 2).mean()
    print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
    print('The Root Mean Squared Error of our forecasts is {}'.format(round(np.sqrt(mse), 2)))


def predict(dataframe, model, step_count):
    pred_uc = model.get_forecast(steps=step_count)
    # Get confidence intervals of forecasts
    pred_ci = pred_uc.conf_int()
    ax = dataframe.plot(label='observed', figsize=(20, 15))
    pred_uc.predicted_mean.plot(ax=ax, label='forecast')
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.25)
    ax.set_xlabel('Date')
    ax.set_ylabel('NAV Levels')
    plt.legend()
    plt.show()
