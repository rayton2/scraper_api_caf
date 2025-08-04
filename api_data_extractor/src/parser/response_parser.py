# response_parser.py

"""
response_parser.py

This module is responsible for parsing JSON responses from the API into usable Python dictionaries or lists.
It includes functions that take raw JSON data and extract relevant information for further processing.
"""

import json
from typing import List, Dict

def parse_municipios_response(response: str) -> List[Dict]:
    """
    Parses the JSON response for municipalities.

    Args:
        response (str): The raw JSON response as a string.

    Returns:
        List[Dict]: A list of dictionaries containing municipality data.
    """
    try:
        data = json.loads(response)
        municipios = data.get('municipios', [])
        return municipios
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []

def parse_consulta_publica_response(response: str) -> List[Dict]:
    """
    Parses the JSON response for public consultation data.

    Args:
        response (str): The raw JSON response as a string.

    Returns:
        List[Dict]: A list of dictionaries containing public consultation data.
    """
    try:
        data = json.loads(response)
        consultas = data.get('consultas', [])
        return consultas
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []