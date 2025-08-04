# api_data_extractor

## Overview
The `api_data_extractor` project is designed to provide a modular data extraction pipeline that interfaces with a RESTful API to retrieve and store data efficiently. This project replaces a previous Selenium-based scraper with a more reliable and faster API data extraction system.

## Project Structure
The project is organized into several modules, each responsible for a specific aspect of the data extraction process:

- `src/main.py`: The entry point of the application that orchestrates the data extraction process.
- `src/client/api_client.py`: Handles all HTTP requests to the CAF API, abstracting endpoints for fetching municipalities and public consultation data.
- `src/parser/response_parser.py`: Parses JSON responses from the API into usable Python dictionaries or lists.
- `src/storage/excel_writer.py`: Saves structured data into an Excel file (XLSX format).
- `src/config/settings.py`: Contains configuration settings such as base URLs, headers, and constants.

## Setup Instructions
1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd api_data_extractor
   ```

2. **Install required packages**:
   Ensure you have Python installed, then install the necessary libraries using pip:
   ```
   pip install requests openpyxl
   ```

3. **Run the application**:
   Execute the main script to start the data extraction process:
   ```
   python src/main.py
   ```

## Usage Guidelines
- The application fetches all municipalities from the endpoint `/api/municipios?uf=GO`.
- For each municipality, it retrieves paginated results from `/api/ufpa/consulta-publica?uf=GO&codigoMunicipio={codigo}&pagina=1&tamanhoPagina=9999`.
- The extracted data is parsed and saved into an Excel file named `output.xlsx`, located in the `data/` folder.

## Future Enhancements
This project is designed to be easily extendable for future endpoints. Developers can add new modules or extend existing ones to accommodate additional data sources or processing requirements.

## License
This project is licensed under the MIT License - see the LICENSE file for details.