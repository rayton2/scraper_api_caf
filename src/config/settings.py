# Configuration settings for the API data extractor project

# Base URL for the CAF API
BASE_URL = "https://caf.mda.gov.br"

# Default headers for HTTP requests
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# Constants for UF codes
UF_CODE_GO = "TO"

# Pagination settings
DEFAULT_PAGE_SIZE = 9999
DEFAULT_PAGE_NUMBER = 1