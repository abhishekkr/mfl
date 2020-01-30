# provide data modifying common helper functions
import logging
from datetime import datetime


def fill_null(dataframe):
    return dataframe.fillna(dataframe.bfill()) # taking care of null fields


def null_date_converter(value):
    try:
        return datetime.strptime(value, "%d-%m-%Y").date()
    except:
        logging.warning("failed date conversion in dataframe for: %s" % (value))
        return None
