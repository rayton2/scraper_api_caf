# response_parser.py
import json
from typing import List, Dict

def parse_municipios_response(response: dict) -> List[Dict]:
    try:
        municipios = response.get('municipios', [])
        return municipios
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []

def parse_consulta_publica_response(response: str) -> List[Dict]:
    try:
        data = json.loads(response)
        consultas = data.get('consultas', [])
        return consultas
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []