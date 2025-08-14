# api_client.py

import requests
from config.settings import BASE_URL, HEADERS
import time

class APIClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = HEADERS

    def get_municipios(self, uf):
        endpoint = f"{self.base_url}/api/municipios?uf={uf}"
        response = self._get_request(endpoint)
        return response

    def get_consulta_publica(self, uf, pagina=1, tamanho_pagina=9999):
        endpoint = f"{self.base_url}/api/ufpa/consulta-publica?uf={uf}&pagina={pagina}&tamanhoPagina={tamanho_pagina}"
        # time.sleep(10)
        response = self._get_request(endpoint)
        return response

    def _get_request(self, url):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request failed: {e}")
            return {}