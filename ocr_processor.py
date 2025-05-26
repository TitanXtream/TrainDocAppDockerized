from pdf2image import convert_from_path
# from PIL.Image import Image
# import os
# import numpy as np
# # from google.colab import files
from paddleocr import PaddleOCR
# import cv2
# from typing import LiteralString

# # uploaded_files = files.upload()
# # image_paths = list(uploaded_files.keys())

# # STEP 4: Initialize OCR engines
# # tesseract_results = {}
# # paddle_results = {}


# def preprocess_image(image: Image):
#     # 1. Convert to grayscale
#     gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

#     # 2. Denoising using GaussianBlur
#     denoised_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

#     # 3. Binarization using Otsu's thresholding
#     _, binarized_image = cv2.threshold(
#         denoised_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

#     return binarized_image


# def pdf_to_image(file_path, dpi=300):
#     images = convert_from_path(file_path, dpi=300)

#     # png_images = [image.convert('RGB') for image in images]

#     # return png_images
#     # preprocessed_images = [preprocess_image(image) for image in images]

#     return images


# # def preporcess_image(image:)


# def extract_ocr_text(images: list[Image]):

#     paddle_ocr = PaddleOCR(lang='en')

#     paddler_results: list[LiteralString] = []


# # # STEP 5: OCR Processing Loop
# # os.makedirs("ocr_output", exist_ok=True)

#     for image in images:

#         processed_image = preprocess_image(image)
#         # Load image
#         # image = Image.open(img_path)

#         # # --- Tesseract OCR ---
#         # tesseract_text = pytesseract.image_to_string(image)
#         # tesseract_results[img_path] = tesseract_text

#         # # Save Tesseract output
#         # with open(f"ocr_output/{os.path.basename(img_path)}_tesseract.txt", "w") as f:
#         #     f.write(tesseract_text)

#         # --- PaddleOCR ---
#         result = paddle_ocr.predict(processed_image)
#         paddle_text_lines = []
#         for res in result:
#             for line in res:
#                 if line == "rec_texts":
#                     # Extract recognized text
#                     paddle_text_lines.append(res[line])

#         paddle_text = " ".join(paddle_text_lines)
#         # paddle_results[image.] = paddle_text

#         print("\n--- PaddleOCR Output - Start ---\n")
#         print(paddle_text)
#         print("\n--- PaddleOCR Output - End ---\n")

#         # return paddle_text
#         paddler_results.append(paddle_text)
#         # Save PaddleOCR output
#         # with open(f"ocr_output/{os.path.basename(img_path)}_paddleocr.txt", "w") as f:
#         #     f.write(paddle_text)
#     return paddler_results
#     # STEP 6: Display a quick comparison
#     # for image in images:
#     #     print("="*50)
#     #     # print("\n--- Tesseract OCR Output ---\n")
#     #     # print(tesseract_results[img_path])
#     #     print("\n--- PaddleOCR Output ---\n")
#     #     print(paddle_results[img_path])

def test_func():
    pass
