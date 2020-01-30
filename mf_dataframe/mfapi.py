# to provide functionality on usage of api.mfapi.in
import requests


def mf_json_from_url(mf_url):
    r = requests.get(mf_url)
    return r.json()['data']
