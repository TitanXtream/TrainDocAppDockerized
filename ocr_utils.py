
import pytesseract
from pdf2image import convert_from_path
import re
from custome_types import BillFields

def ocr_pdf(file_path):
    images = convert_from_path(file_path)
    full_text = ""
    for img in images:
        full_text += pytesseract.image_to_string(img, lang="deu") + "\n"
    return full_text

def extract_fields(text):
    # wagon = re.findall(r'Waggon(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    datum = re.findall(r'Datum\s*\:?\s*(\d{2}\.\d{2}\.\d{4})', text, re.IGNORECASE)
    schicht = re.findall(r'Schicht(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    ladung = re.findall(r'Ladung(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    uhrzeit = re.findall(r'zu\s*(\d{2}:\d{2})\s*Uhr', text, re.IGNORECASE)
    gleis = re.findall(r'Gleis(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    anzahl = re.findall(r'Anzahl(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    zuge_waggons = re.findall(r'Züge / Waggons(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    abfahrt = re.findall(r'Abfahrt(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    datum_uhrzeit = re.findall(r'Datum/Uhrzeit Leer/Voll(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    uhrzeit = re.findall(r'DB Uhrzeit(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)', text, re.IGNORECASE)
    begrundung = re.findall(r"Begründung(?:s)?(?: No)?\.?\:?[\s\-]*(\w+)", text, re.IGNORECASE)
    # status = re.findall(r'Status\:?[\s]*([A-Za-z]+)', text, re.IGNORECASE)
    # r'.*?\d{2}:\d{2}.*'

    return {
        # "wagon": wagon[0] if wagon else "N/A",
        "Datum": datum[0] if datum else "N/A",
        "Schicht": schicht[0] if schicht else "N/A",
        "Ladung": ladung[0] if ladung else "N/A",
        "JM Uhrzeit": uhrzeit[0] if uhrzeit else "N/A",
        "Gleis": gleis[0] if gleis else "N/A",
        "Anzahl": anzahl[0] if anzahl else "N/A",
        "Züge / Waggons":zuge_waggons[0] if zuge_waggons else "N/A",
        "Abfahrt":abfahrt[0] if abfahrt else "N/A",
        "Datum/Uhrzeit Leer/Voll":datum_uhrzeit[0] if datum_uhrzeit else "N/A",
        "DB Uhrzeit": uhrzeit[0] if uhrzeit else "N/A",
        "Begründung": begrundung[0] if begrundung else "N/A"
        # "status": status[0] if status else "N/A"
    }
