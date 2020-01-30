# provide resampling helpers

from . import mod

def day_sample_dataframe(dataframe):
    df_day = dataframe.resample('D').mean()
    return mod.fill_null(df_day)


def bizday_sample_dataframe(dataframe):
    df_bizday = dataframe.resample('B').mean()
    return mod.fill_null(df_bizday)


def weekly_sample_dataframe(dataframe):
    df_weekly = dataframe.resample('W').mean()
    return mod.fill_null(df_weekly)


def monthly_sample_dataframe(dataframe):
    df_monthly = dataframe.resample('MS').mean()
    return mod.fill_null(df_monthly)
