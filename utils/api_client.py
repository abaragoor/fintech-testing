import requests
from utils.config import Config
from utils.logger import log, log_response

class ApiClient:
    def __init__(self, base_url=None):
        self.base_url = base_url or Config.BASE_URL.rstrip('/')

    def _url(self, endpoint):
        if not endpoint.startswith('/'):
            endpoint = '/' + endpoint
        return f"{self.base_url}{endpoint}"

    def post(self, endpoint, payload, headers=None):
        url = self._url(endpoint)
        log(f"POST {url} - payload={payload}")
        resp = requests.post(url, json=payload, headers=headers)
        log_response(resp)
        return resp

    def get(self, endpoint, headers=None, params=None):
        url = self._url(endpoint)
        log(f"GET {url} - params={params}")
        resp = requests.get(url, headers=headers, params=params)
        log_response(resp)
        return resp
