#
from . import mfapi
from . import urls_from_mfapi_in

def json_from_url(url):
    return mfapi.mf_json_from_url(url)

def api_from_mfapi_in(fund_name):
    return urls_from_mfapi_in.sbi_direct_growth[fund_name]
