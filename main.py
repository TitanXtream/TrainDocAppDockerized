import os
from ocr_utils import ocr_pdf, extract_fields
from excel_writer import write_to_excel

INPUT_DIR = "downloads"

def main():
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]
    results = []

    for file in files:
        full_path = os.path.join(INPUT_DIR, file)
        print(f"Processing {file}...")
        text = ocr_pdf(full_path)
        fields = extract_fields(text)
        print(f"Extracted: {fields}")
        results.append(fields)

    write_to_excel(results)
    print("✅ Done. Data written to output.xlsx")

if __name__ == "__main__":
    main()
