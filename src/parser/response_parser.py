# response_parser.py
import json
from typing import List, Dict

def parse_municipios_response(response) -> List[Dict]:
    try:
        if isinstance(response, list):
            return response
        elif isinstance(response, dict):
            # Tenta encontrar a chave correta
            if "municipios" in response:
                return response["municipios"]
            elif "data" in response:
                return response["data"]
            else:
                # Se não encontrar, tenta extrair lista de dicts
                return [v for v in response.values() if isinstance(v, list)]
        else:
            return []
    except Exception as e:
        print(f"Erro ao processar resposta dos municípios: {e}")
        return []

def parse_consulta_publica_response(response: dict) -> List[Dict]:
    try:
        consultas = response.get('consultas', [])
        return consultas
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []