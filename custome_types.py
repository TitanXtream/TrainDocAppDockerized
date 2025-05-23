from typing import TypedDict

headings = ["Datum","Schicht","Ladung","JM Uhrzeit","Gleis","Anzahl","Züge / Waggons","Abfahrt","Datum/Uhrzeit Leer/Voll","DB Uhrzeit","Begründung"]

BillFields = TypedDict("BillFields", {key: str for key in headings})