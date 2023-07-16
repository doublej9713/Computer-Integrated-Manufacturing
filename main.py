import pytesseract
import cv2
import re
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

# Specify the path to your invoice image
invoice_image_paths = [".\image\invoice1.png", ".\image\invoice2.jpg"]

def extract_information(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Perform OCR
    text = pytesseract.image_to_string(image)

    # Process the text to filter out unwanted line breaks
    cleaned_text = text.replace('\n', ' ')

    # Extract information using regular expressions
    invoice_number = re.search(r"Invoice\s*(?:#|No\.|no\.|Number)[:\s]*(\S+)", cleaned_text, re.IGNORECASE)
    invoice_date = re.search(r"(?i)(?:Issue|Invoice)\s*Date[:\s]*([\d/]+\s+\w+\s+\d{4}|\d{1,2}/\d{1,2}/\d{4})",cleaned_text)
    grand_total = re.search(r"(?i)(?:Invoice\s+total|Total\s+due|balance\s+due|Total)[:\s]*([0-9.,]+)", cleaned_text,re.IGNORECASE)

    # Process extracted information
    extracted_info = {}
    if invoice_number:
        extracted_info["Invoice Number"] = invoice_number.group(1)
    if invoice_date:
        extracted_info["Invoice Date"] = invoice_date.group(1)
    if grand_total:
        extracted_info["Grand Total"] = grand_total.group(1)

    return extracted_info


for image_path in invoice_image_paths:
    # Extract information from the invoice image
    invoice_info = extract_information(image_path)

    # Print the extracted information
    print("Extracted Information:")
    for key, value in invoice_info.items():
        print(key + ":", value)