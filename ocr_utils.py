# import pytesseract
# from pdf2image import convert_from_path
# import re

# def ocr_pdf(file_path):
#     images = convert_from_path(file_path)
#     full_text = ""
#     for img in images:
#         full_text += pytesseract.image_to_string(img) + "\n"
#     return full_text

# def extract_fields(text):
#     wagon = re.findall(r'Wagon(?: No)?\.?:?\s?(\d+)', text)
#     date = re.findall(r'Date:? (\d{2}/\d{2}/\d{4})', text)
#     status = re.findall(r'Status:? ([A-Za-z]+)', text)
#     return {
#         "wagon": wagon[0] if wagon else "N/A",
#         "date": date[0] if date else "N/A",
#         "status": status[0] if status else "N/A"
#     }

import pytesseract
from pdf2image import convert_from_path
import re
from custome_types import BillFields

def ocr_pdf(file_path):
    images = convert_from_path(file_path)
    full_text = ""
    for img in images:
        full_text += pytesseract.image_to_string(img, lang="deu") + "\n"
        # print(full_text)
        # print("\n\n")
    return full_text

def extract_fields(text):
    wagon = re.findall(r'Waggon(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    datum = re.findall(r'Datum\s*\:?\s*(\d{2}\.\d{2}\.\d{4})', text, re.IGNORECASE)
    schicht = re.findall(r'Schicht(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    ladung = re.findall(r'Ladung(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    uhrzeit = re.findall(r'zu\s*(\d{2}:\d{2})\s*Uhr', text, re.IGNORECASE)
    gleis = re.findall(r'Gleis(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    # status = re.findall(r'Status\:?[\s]*([A-Za-z]+)', text, re.IGNORECASE)
    # r'.*?\d{2}:\d{2}.*'

    return {
        # "wagon": wagon[0] if wagon else "N/A",
        "Datum": datum[0] if datum else "N/A",
        "Schicht": schicht[0] if schicht else "N/A",
        "Ladung": ladung[0] if ladung else "N/A",
        "Uhrzeit": uhrzeit[0] if uhrzeit else "N/A",
        "Gleis": gleis[0] if gleis else "N/A"
        # "status": status[0] if status else "N/A"
    }
