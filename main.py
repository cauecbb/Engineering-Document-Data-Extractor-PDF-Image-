import pytesseract
import cv2
import numpy as np
from pdf2image import convert_from_path
import os
import re
import pandas as pd

def process_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    full_text = ""
    for img in images:
        image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        text = pytesseract.image_to_string(thresh)
        full_text += text + "\n"
    return full_text

def extract_data(text):
    def find(pattern):
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1).strip() if match else None

    data = {
        "component": find(r'Component[:\-]?\s*(.*)'),
        "tag": find(r'Tag[:\-]?\s*(\S+)'),
        "material": find(r'Material[:\-]?\s*([\w\s\-]+)'),
        "operating_pressure": find(r'Operating Pressure[:\-]?\s*([\d.,]+)'),
        "maximum_pressure": find(r'Maximum Pressure[:\-]?\s*([\d.,]+)'),
        "maximum_temperature": find(r'Maximum Temperature[:\-]?\s*([\d.,]+)'),
        "manufacturer": find(r'Manufacturer[:\-]?\s*(.*)'),
        "model": find(r'Model[:\-]?\s*([\w\-]+)')
    }
    return data

def main():
    results = []
    for file in os.listdir("samples"):
        if file.lower().endswith((".pdf", ".jpg", ".png", ".jpeg")):
            print(f"🔍 Processing {file}")
            text = process_pdf(os.path.join("samples", file))
            data = extract_data(text)
            data['file'] = file
            results.append(data)

    df = pd.DataFrame(results)
    df.to_csv("output/result.csv", index=False)
    df.to_json("output/result.json", orient="records", indent=4)
    print("✅ Done! Check the 'output' folder for results.")

if __name__ == "__main__":
    main()
