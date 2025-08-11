# response_parser.py
import json
from typing import List, Dict

def parse_municipios_response(response) -> List[Dict]:
    try:
        if isinstance(response, dict):
            # Extrai da chave 'dados'
            municipios = response.get('dados', [])
            if isinstance(municipios, list):
                return [item for item in municipios if isinstance(item, dict)]
        elif isinstance(response, list):
            return [item for item in response if isinstance(item, dict)]
        return []
    except Exception as e:
        print(f"Erro ao processar resposta dos municípios: {e}")
        return []

def parse_consulta_publica_response(response: dict) -> List[Dict]:
    try:
        consultas = response.get('dados', [])
        return consultas
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []