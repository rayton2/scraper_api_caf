# response_parser.py
import json
from typing import List, Dict

def parse_municipios_response(response: dict) -> List[Dict]:
    try:
        # Supondo que 'response' seja um dict que já contém os dados dos municípios
        return response if isinstance(response, list) else response.get("municipios", [])
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