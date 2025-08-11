# Entry point for the API data extraction application

import os
from client.api_client import APIClient
from parser.response_parser import parse_municipios_response, parse_consulta_publica_response
from storage.excel_writer import save_to_excel
from config.settings import DEFAULT_PAGE_SIZE
import time

def main():
    print("Iniciando extração via API...")
    api_client = APIClient()

    # Step 1: Get all municipalities
    print("Buscando lista de municípios...")
    municipios_response = api_client.get_municipios(uf='GO')
    print("Tipo do response:", type(municipios_response))
    print("municipios_response:", municipios_response)
    #print("Exemplo de município:", municipios_response[0] if municipios_response else "Lista vazia")
    #municipios = municipios_response.get('municipios', [])
    municipios = parse_municipios_response(municipios_response)
    print(f"Total de municípios encontrados: {len(municipios)}")
    print("Exemplo de município:", municipios[0] if municipios else "Lista vazia")

    # Step 2: Iterate through each municipality and fetch paginated results
    all_data = []
    for municipio in municipios:
        codigo = municipio['codigoMunicipio']
        print(f"Buscando dados para município {codigo}")
        page = 1
        while True:
            print(f"Buscando município {municipio['nome']} (código: {codigo}), página {page}...")

            consulta_response = api_client.get_consulta_publica(
                uf='GO', 
                codigo_municipio=codigo, 
                pagina=page,
                tamanho_pagina=DEFAULT_PAGE_SIZE
            )
            print("Resposta da API:", consulta_response) 

            parsed_data = parse_consulta_publica_response(consulta_response)
            print(f"Dados extraídos nesta página: {len(parsed_data)} registros")

            if not parsed_data:
                print("Sem dados nesta página. Encerrando loop.")
                break  # Exit loop if no more data is available

            all_data.extend(parsed_data)
            if len(parsed_data) < DEFAULT_PAGE_SIZE:
                print("Última página alcançada. Encerrando loop.")
                break
            
            page += 1  # Increment page for next request
            time.sleep(5)
        time.sleep(10)

    print(f"Total de registros coletados: {len(all_data)}")

    # Step 3: Write results into an Excel file
    os.makedirs('data', exist_ok=True)
    output_file_path = os.path.join('data', 'output.xlsx')
    save_to_excel(all_data, output_file_path)
    print(f"Dados salvos em {output_file_path}")

if __name__ == "__main__":
    main()