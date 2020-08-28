#!python3
"""
to predict Mutual Fund NAV
reference:
    * https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-visualization-with-python-3
    * https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3
    * https://towardsdatascience.com/an-end-to-end-project-on-time-series-analysis-and-forecasting-with-python-4835e6bf050b
"""

import sys

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

import mf_dataframe


### helper
def help():
    print("""
            you need help,
            usage:
            python mfl.py <showtime> [<full fund name>]
            python mfl.py <diff> [<full fund name>]
            """)


### main

if __name__ == '__main__':
    fund_name = 'nifty index fund'
    run_mode = "showtime"
    if len(sys.argv) > 1:
        run_mode = sys.argv[1]
        if len(sys.argv) > 2:
            fund_name = sys.argv[2]

    if run_mode == "showtime":
        mf_dataframe.showtime_from_mfapi_in(fund_name)
    elif run_mode == "diff":
        print("diff will run here")
    else:
        help()
