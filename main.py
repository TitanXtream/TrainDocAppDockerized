import os
# from ocr_processor import pdf_to_image, extract_ocr_text
from ocr_processor import test_func

INPUT_DIR = "input"
OUTPUT_DIR = "output"


def main():
    # files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".pdf")]
    # results = []

    # for file in files:
    #     full_path = os.path.join(INPUT_DIR, file)
    #     print(f"Processing {file}...")

    #     # pdf to image
    #     images = pdf_to_image(full_path)

    #     # Image pre process + Text extraction with paddle
    #     paddler_texts = extract_ocr_text(images)

    #     print("Extracted texts ...")
    #     print("\n".join(paddler_texts))

    #     print(
    #         f"Processing complete File: {file} (Text extracted successfully)")
    # print("Hi there")

    # Image pre process

    # Text extraction with paddle

    # Convert to structured json

    # Deviation calculation flag

    # Log events

    # Give output in excell
    test_func()
    pass


if __name__ == "__main__":
    main()
