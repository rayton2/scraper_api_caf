# excel_writer.py
import openpyxl
from openpyxl.utils import get_column_letter
from typing import List, Dict, Any

def save_to_excel(data, file_path='data/output_DF.xlsx') -> None:
    if not data or not isinstance(data[0], dict):
        print("Nenhum dado válido para salvar.")
        return
    # Create a new workbook and select the active worksheet
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # Write the header row
    headers = list(data[0].keys())
    worksheet.append(headers)

    # Write the data rows
    for item in data:
        worksheet.append([item.get(key, "") for key in headers])

    workbook.save(file_path)