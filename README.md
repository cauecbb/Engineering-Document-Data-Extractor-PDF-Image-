# 📄 Engineering Document Data Extractor

Extract structured data from engineering documents (PDF/images) using OCR and image processing.

## 🚀 Features

- PDF to image conversion
- OCR text extraction with Tesseract
- Automatic data extraction (components, tags, materials, pressures, temperatures)
- Output in CSV and JSON formats
- Docker support

## 🛠️ Tech Stack

- **Python 3.11** + OpenCV + Tesseract OCR + PDF2Image + Pandas
- **Docker** for easy deployment

## 🔧 Quick Start

### Option 1: Docker (Recommended)
```bash
git clone https://github.com/your-username/Engineering-Document-Data-Extractor-PDF-Image-.git
cd Engineering-Document-Data-Extractor-PDF-Image-
docker build -t engineering-doc-extractor .
docker run -v $(pwd)/samples:/app/samples -v $(pwd)/output:/app/output engineering-doc-extractor
```

### Option 2: Local Installation
```bash
# Install system dependencies
# Windows: Download Tesseract OCR and Poppler
# Linux: sudo apt-get install tesseract-ocr poppler-utils libgl1
# macOS: brew install tesseract poppler

# Install Python dependencies
pip install -r requirements.txt

# Run
python main.py
```

## 📁 Usage

1. Add PDF/images to `samples/` folder
2. Run the program
3. Check results in `output/` folder

## 📊 Output

Extracts: Component, Tag, Material, Operating Pressure, Maximum Pressure, Maximum Temperature, Manufacturer, Model

**CSV Example:**
```csv
file,component,tag,material,operating_pressure,maximum_pressure,maximum_temperature,manufacturer,model
sample.pdf,Valve,V-101,Stainless Steel,150,300,200,ABC Corp,VAL-001
```

## 🎯 Extraction Patterns

Looks for: `Component: [value]`, `Tag: [value]`, `Material: [value]`, `Operating Pressure: [value]`, etc.

## 🐛 Troubleshooting

- **"tesseract not found"**: Install Tesseract OCR
- **"poppler not found"**: Install Poppler-utils
- **Low OCR quality**: Check document resolution, adjust threshold in code

