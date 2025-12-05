# PDF Utilities

A collection of utilities for working with PDF files, including conversion from images and text extraction with text-to-speech capabilities.

## Features

- Convert multiple images to a single PDF document
- Extract text from PDF files
- Convert PDF text to speech audio
- Batch processing support
- Error handling and validation
- Cross-platform compatibility
- Comprehensive logging

## Files

### image2pdf.py

**Purpose:** Convert image files (PNG, JPG, JPEG) to PDF documents.

**Features:**

- Batch process multiple images
- Support for various image formats
- Configurable output directory
- Automatic file discovery
- Error handling for invalid images

**Usage:**

```bash
# Convert all images in current directory
python image2pdf.py

# Specify input directory and output file
python image2pdf.py --directory /path/to/images/ --output result.pdf

# Process images in current directory
python image2pdf.py --directory . --output combined.pdf
```

### read_pdf.py

**Purpose:** Extract text from PDF files and convert to speech.

**Features:**

- Extract text from single or multiple pages
- Text-to-speech conversion
- Configurable voice selection (male/female)
- Adjustable speech rate
- File dialog support for easy file selection
- Batch processing capabilities

**Usage:**

```bash
# Interactive file selection
python read_pdf.py

# Specify PDF file
python read_pdf.py --file document.pdf

# Extract text and convert to speech
python read_pdf.py --file document.pdf --output audio.mp3

# Use specific voice (0=default, 1=alternative)
python read_pdf.py --file document.pdf --voice 1
```

## Installation

### Prerequisites

- Python 3.12+
- pip or conda

### Required Packages

```bash
pip install PyPDF2 img2pdf pyttsx3 pillow
```

## Supported Formats

### Image Formats (image2pdf.py)

- PNG (.png)
- JPEG (.jpg, .jpeg)
- BMP (.bmp)
- GIF (.gif)
- TIFF (.tiff)

### PDF Formats (read_pdf.py)

- Standard PDF files
- Text-based PDFs
- Multi-page documents

## Performance

- **Image to PDF:** ~100-500ms per image depending on size
- **PDF Text Extraction:** ~50-200ms per page
- **Text-to-Speech:** Depends on text length (typically real-time)
- **Memory Usage:** <100MB for typical operations

## Troubleshooting

### Image2PDF Issues

**Problem:** "No images found"

- **Solution:** Verify image directory exists and contains supported formats

**Problem:** "Permission denied"

- **Solution:** Check write permissions for output directory

### Read_PDF Issues

**Problem:** "PyPDF2 not found"

- **Solution:** Install with `pip install PyPDF2`

---

**Last Updated:** December 2025
