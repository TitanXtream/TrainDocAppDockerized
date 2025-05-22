from openpyxl import Workbook
from custome_types import headings

def write_to_excel(data_list, file_path="output.xlsx"):
    wb = Workbook()
    ws = wb.active
    ws.append(headings)
    for row in data_list:
        heading_column = [row[h] for h in headings]
        ws.append(heading_column)
        # ws.append(["wagon", "date", "status"])
    wb.save(file_path)