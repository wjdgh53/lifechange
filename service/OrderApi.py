import requests
from config.config import API_URL
from service.Authentication import get_binanceus_signature



def apiheaders(api_key):
    headers = {}
    headers['X-MBX-APIKEY'] = api_key
    return headers

# Attaches auth headers and returns results of a POST request
def binanceus_request(uri_path, data, api_key, api_sec):
    signature = get_binanceus_signature(data, api_sec)
    params={**data, "signature": signature}
    req = requests.get((API_URL + uri_path), params=params, headers=apiheaders(api_key))
    return req.text
data = {
    "symbol": "BTCUSDT",
    "timestamp": 1499827319559
}