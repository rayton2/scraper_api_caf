# Configuration settings for the API data extractor project

# Base URL for the CAF API
BASE_URL = "https://api.example.com"

# Endpoints for the API
MUNICIPIOS_ENDPOINT = "/api/municipios"
CONSULTA_PUBLICA_ENDPOINT = "/api/ufpa/consulta-publica"

# Default headers for HTTP requests
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Constants for UF codes
UF_CODE_GO = "GO"

# Pagination settings
DEFAULT_PAGE_SIZE = 9999
DEFAULT_PAGE_NUMBER = 1