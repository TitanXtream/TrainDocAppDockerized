from typing import TypedDict

headings = ["Datum","Schicht","Ladung"]

BillFields = TypedDict("BillFields", {key: str for key in headings})