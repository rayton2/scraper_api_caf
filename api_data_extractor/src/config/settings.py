# Configuration settings for the API data extractor project

# Base URL for the CAF API
BASE_URL = "https://caf.mda.gov.br/consulta-publica/ufpa"

# Endpoints for the API
MUNICIPIOS_ENDPOINT = "https://caf.mda.gov.br/api/municipios?uf=GO"
CONSULTA_PUBLICA_ENDPOINT = "https://caf.mda.gov.br/api/ufpa/consulta-publica?uf=GO&codigoMunicipio=5200050&pagina=1&tamanhoPagina=9999"

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