# excel_writer.py
import openpyxl
from openpyxl.utils import get_column_letter
from typing import List, Dict, Any

def save_to_excel(data, file_path='data/output.xlsx') -> None:
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

    # Auto-adjust column widths
    for col_idx, column_cells in enumerate(worksheet.iter_cols(min_row=1, max_row=worksheet.max_row), start=1):
        max_length = 0
        for cell in column_cells:
            value = str(cell.value) if cell.value is not None else ""
        if len(value) > max_length:
            max_length = len(value)
        adjusted_width = max_length + 2
        worksheet.column_dimensions[get_column_letter(col_idx)].width = adjusted_width

    workbook.save(file_path)