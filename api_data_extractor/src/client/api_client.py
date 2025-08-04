# api_client.py

import requests
from config.settings import BASE_URL, HEADERS

class APIClient:
    """Handles HTTP requests to the CAF API."""

    def __init__(self):
        """Initializes the API client with base URL and headers."""
        self.base_url = BASE_URL
        self.headers = HEADERS

    def get_municipios(self, uf):
        """
        Fetches all municipalities for a given UF.

        Args:
            uf (str): The UF code to fetch municipalities for.

        Returns:
            dict: JSON response containing municipalities data.
        """
        endpoint = f"{self.base_url}/api/municipios?uf={uf}"
        response = self._get_request(endpoint)
        return response

    def get_consulta_publica(self, uf, codigo_municipio, pagina=1, tamanho_pagina=9999):
        """
        Fetches public consultation data for a specific municipality.

        Args:
            uf (str): The UF code.
            codigo_municipio (str): The municipality code.
            pagina (int): The page number for pagination.
            tamanho_pagina (int): The number of results per page.

        Returns:
            dict: JSON response containing public consultation data.
        """
        endpoint = f"{self.base_url}/api/ufpa/consulta-publica?uf={uf}&codigoMunicipio={codigo_municipio}&pagina={pagina}&tamanhoPagina={tamanho_pagina}"
        response = self._get_request(endpoint)
        return response

    def _get_request(self, url):
        """
        Makes a GET request to the specified URL.

        Args:
            url (str): The URL to send the GET request to.

        Returns:
            dict: JSON response from the API.

        Raises:
            Exception: If the request fails or returns an error.
        """
        response = requests.get(url, headers=self.headers)
        if response.status_code != 200:
            raise Exception(f"Error fetching data: {response.status_code} - {response.text}")
        return response.json()