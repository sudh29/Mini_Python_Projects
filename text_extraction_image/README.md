# Text Extraction from Images (OCR)

Utilities for extracting text from image files using Optical Character Recognition (OCR) technology.

## Features

- Extract text from JPEG and PNG images
- Multi-language text detection and recognition
- Configurable output formatting
- Batch processing capabilities
- Support for rotated and skewed text
- High accuracy text recognition
- Error handling for invalid images

## Files

### image_to_text.py

**Purpose:** Convert image files to text using the Tesseract OCR engine.

**Features:**

- Read image files from disk
- Process single or multiple images
- Extract complete text content
- Handle various image formats
- Error handling for invalid images
- Support for pre-processing (grayscale, contrast adjustment)

**Usage:**

```bash
python image_to_text.py --image path/to/image.jpg
python image_to_text.py --directory path/to/images/
```

**Example:**

```python
from image_to_text import extract_text_from_image
text = extract_text_from_image('document.png')
print(text)
```

---

## Installation

### Prerequisites

- Python 3.12+
- Tesseract OCR engine

### Setup

1. Install Tesseract OCR:

```bash
# Ubuntu/Debian
sudo apt-get install tesseract-ocr

# macOS
brew install tesseract

# Windows
# Download from https://github.com/UB-Mannheim/tesseract/wiki
```

2. Install Python dependencies:

```bash
pip install pytesseract pillow
```

## Supported Image Formats

- JPEG (.jpg, .jpeg)
- PNG (.png)
- BMP (.bmp)
- TIFF (.tiff)
- WebP (.webp)

## Usage Examples

```python
# Extract text from a single image
python image_to_text.py --image document.jpg

# Process all images in a directory
python image_to_text.py --directory ./images/

# Save output to file
python image_to_text.py --image document.jpg --output result.txt
```

## Requirements

```
pytesseract>=0.3.10
pillow>=10.0
```

## Performance

- **Average Processing Time:** 0.5-2 seconds per image
- **Memory Usage:** ~50-100MB
- **Maximum Image Size:** No strict limit (depends on system memory)

## Troubleshooting

### Tesseract not found error

Ensure Tesseract is installed and in your system PATH. On Windows, you may need to specify the installation path:

```python
import pytesseract
pytesseract.pytesseract.pytesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Low accuracy results

- Ensure image quality is high (300+ DPI recommended)
- Try pre-processing images (convert to grayscale, increase contrast)
- Specify language code for better recognition

---

**Last Updated:** December 2025
