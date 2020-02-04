# to provide functionality on usage of api.mfapi.in
import logging
import requests
import base64
import datetime
from datetime import date

from . import fs


RELATIVE_PATH = 'mfapi'

SOURCE_URL_KEY = 'source_url'
LAST_FETCH_TIMESTAMP_KEY = 'on_date'


def mf_json_from_url(mf_url):
    today = date.today()
    filename = "%s.json" % (b64encode(mf_url))
    file_json = fs.read_json(RELATIVE_PATH, filename)
    if SOURCE_URL_KEY in file_json.keys():
        if file_json[SOURCE_URL_KEY] != mf_url:
            raise 'pre-existing file with wrong source url'
    if LAST_FETCH_TIMESTAMP_KEY in file_json.keys():
        if file_json[LAST_FETCH_TIMESTAMP_KEY] == date_string(today):
            return file_json['data']
    logging.debug('no cache found for url: %s' % (mf_url))
    print('..........')
    json_data = fetch_from_url(mf_url)
    json_data[SOURCE_URL_KEY] = mf_url
    json_data[LAST_FETCH_TIMESTAMP_KEY] = date_string(today)
    fs.dump_json(RELATIVE_PATH, filename, json_data)
    return json_data['data']


def fetch_from_url(mf_url):
    r = requests.get(mf_url)
    return r.json()


def date_string(day):
    return day.strftime("%Y-%m-%d")


def b64encode(str_value):
    return str(
        base64.urlsafe_b64encode(
            str_value.encode('ascii')
        ),
        'utf-8'
    )
