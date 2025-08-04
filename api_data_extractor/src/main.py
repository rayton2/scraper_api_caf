# Entry point for the API data extraction application

import os
from client.api_client import APIClient
from parser.response_parser import ResponseParser
from storage.excel_writer import ExcelWriter
from config.settings import BASE_URL, HEADERS

def main():
    """
    Main function to orchestrate the data extraction process.
    It fetches municipalities and their associated data,
    parses the JSON responses, and writes the results to an Excel file.
    """
    api_client = APIClient(BASE_URL, HEADERS)
    response_parser = ResponseParser()
    excel_writer = ExcelWriter()

    # Step 1: Get all municipalities
    municipios_response = api_client.get_municipios(uf='GO')
    municipios = response_parser.parse_municipios(municipios_response)

    # Step 2: Iterate through each municipality and fetch paginated results
    all_data = []
    for municipio in municipios:
        codigo = municipio['codigo']
        page = 1
        while True:
            consulta_response = api_client.get_consulta_publica(uf='GO', codigoMunicipio=codigo, pagina=page)
            parsed_data = response_parser.parse_consulta_publica(consulta_response)

            if not parsed_data:
                break  # Exit loop if no more data is available

            all_data.extend(parsed_data)
            page += 1  # Increment page for next request

    # Step 3: Write results into an Excel file
    output_file_path = os.path.join('data', 'output.xlsx')
    excel_writer.write_to_excel(all_data, output_file_path)

if __name__ == "__main__":
    main()