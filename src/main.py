# Entry point for the API data extraction application

import os
from client.api_client import APIClient
from parser.response_parser import parse_municipios_response, parse_consulta_publica_response
from storage.excel_writer import save_to_excel
from config.settings import BASE_URL, HEADERS

def main():
    api_client = APIClient(BASE_URL, HEADERS)

    # Step 1: Get all municipalities
    municipios_response = api_client.get_municipios(uf='GO')
    municipios = parse_municipios_response(municipios_response)

    # Step 2: Iterate through each municipality and fetch paginated results
    all_data = []
    for municipio in municipios:
        codigo = municipio['codigo']
        page = 1
        while True:
            consulta_response = api_client.get_consulta_publica(uf='GO', codigoMunicipio=codigo, pagina=page)
            parsed_data = parse_consulta_publica_response(consulta_response)

            if not parsed_data:
                break  # Exit loop if no more data is available

            all_data.extend(parsed_data)
            page += 1  # Increment page for next request

    # Step 3: Write results into an Excel file
    os.makedirs('data', exist_ok=True)
    output_file_path = os.path.join('data', 'output.xlsx')
    save_to_excel(all_data, output_file_path)

if __name__ == "__main__":
    main()