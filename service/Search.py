import requests
from config.config import API_URL
from service.Authentication import get_binanceus_signature


def apiheaders(api_key):
    headers = {}
    headers['X-MBX-APIKEY'] = api_key
    return headers

# Attaches auth headers and returns results of a POST request
def test_connectivity():
    uri_path = "/api/v3/ping"
    resp = requests.get((API_URL + uri_path))
    return resp.json()

def exchange_info():
    uri_path ="/api/v3/exchangeInfo"
    params={**data}
    resp = requests.get((API_URL + uri_path), params=params)
    return resp.json()

data = {
    "symbol": "BTCUSDT"
}