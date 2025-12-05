"""
Extract text from images using Optical Character Recognition (OCR).

This module provides utilities to perform OCR on image files using Tesseract,
extracting text content with support for multiple languages and preprocessing.

Features:
- Extract text from JPEG, PNG, BMP, and other image formats
- Support for multiple languages
- Image preprocessing (grayscale, contrast adjustment)
- Batch processing of multiple images
- Configurable Tesseract path for different systems
- Error handling and validation
- Logging support

Usage:
    python image_to_text.py --image photo.jpg
    python image_to_text.py --directory ./images/ --output results.txt
"""

import os
import sys
import logging
from pathlib import Path
from typing import Optional, List, Dict

try:
    import pytesseract
    from PIL import Image
except ImportError as e:
    raise ImportError(
        f"Required packages not installed: {str(e)}\n"
        "Install with: pip install pytesseract pillow"
    )


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# Platform-specific Tesseract configuration
if sys.platform == "win32":
    # Windows path - modify if installed elsewhere
    TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if os.path.exists(TESSERACT_PATH):
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


def extract_text_from_image(
    image_path: str,
    language: str = "eng",
    preprocess: bool = False
) -> Optional[str]:
    """
    Extract text from a single image file using OCR.

    Args:
        image_path: Path to the image file
        language: Tesseract language code (default: 'eng')
        preprocess: Whether to apply image preprocessing (default: False)

    Returns:
        str: Extracted text from the image, or None if extraction fails

    Raises:
        FileNotFoundError: If image file doesn't exist
        PIL.UnidentifiedImageError: If file is not a valid image
    """
    if not Path(image_path).exists():
        raise FileNotFoundError(f"Image file not found: {image_path}")

    try:
        logger.info(f"Processing image: {image_path}")
        
        # Open the image
        image = Image.open(image_path)
        
        # Apply preprocessing if requested
        if preprocess:
            image = _preprocess_image(image)
        
        # Extract text using Tesseract
        text = pytesseract.image_to_string(image, lang=language)
        
        if text.strip():
            logger.info(f"Successfully extracted {len(text)} characters")
        else:
            logger.warning("No text detected in image")
        
        return text

    except Exception as e:
        logger.error(f"Error extracting text from image: {str(e)}")
        raise


def _preprocess_image(image: 'Image.Image') -> 'Image.Image':
    """
    Apply preprocessing to improve OCR accuracy.

    Args:
        image: PIL Image object

    Returns:
        Image.Image: Preprocessed image
    """
    from PIL import ImageEnhance, ImageFilter
    
    # Convert to grayscale
    if image.mode != 'L':
        image = image.convert('L')
    
    # Increase contrast
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)
    
    # Apply sharpness
    sharpness_enhancer = ImageEnhance.Sharpness(image)
    image = sharpness_enhancer.enhance(2)
    
    # Apply slight blur to remove noise
    image = image.filter(ImageFilter.MedianFilter())
    
    return image


def extract_text_from_directory(
    directory: str,
    output_file: Optional[str] = None,
    language: str = "eng",
    recursive: bool = False
) -> Dict[str, str]:
    """
    Extract text from all images in a directory.

    Args:
        directory: Path to directory containing images
        output_file: Optional file to save all extracted text
        language: Tesseract language code
        recursive: Whether to process subdirectories

    Returns:
        dict: Dictionary mapping image paths to extracted text

    Raises:
        ValueError: If directory doesn't exist
    """
    if not os.path.isdir(directory):
        raise ValueError(f"Directory not found: {directory}")

    results = {}
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'}
    
    try:
        logger.info(f"Processing directory: {directory}")
        
        # Get all image files
        if recursive:
            image_files = []
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if Path(file).suffix.lower() in image_extensions:
                        image_files.append(os.path.join(root, file))
        else:
            image_files = [
                os.path.join(directory, f)
                for f in os.listdir(directory)
                if Path(f).suffix.lower() in image_extensions
            ]
        
        logger.info(f"Found {len(image_files)} image(s)")
        
        # Process each image
        for idx, image_file in enumerate(sorted(image_files), 1):
            try:
                logger.info(f"[{idx}/{len(image_files)}] Processing {image_file}")
                text = extract_text_from_image(image_file, language)
                results[image_file] = text if text else ""
            except Exception as e:
                logger.warning(f"Failed to process {image_file}: {str(e)}")
                results[image_file] = None
        
        # Save results if output file specified
        if output_file:
            _save_results(results, output_file)
        
        logger.info(f"Successfully processed {len([v for v in results.values() if v])}/{len(image_files)} images")
        return results

    except Exception as e:
        logger.error(f"Error processing directory: {str(e)}")
        return {}


def _save_results(results: Dict[str, str], output_file: str) -> None:
    """
    Save extracted text results to file.

    Args:
        results: Dictionary of image paths to extracted text
        output_file: Path where results will be saved
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            for image_path, text in sorted(results.items()):
                f.write(f"=== {image_path} ===\n")
                if text:
                    f.write(text)
                else:
                    f.write("[No text detected]\n")
                f.write("\n\n")
        
        logger.info(f"Results saved to: {output_file}")
    except Exception as e:
        logger.error(f"Error saving results: {str(e)}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract text from images using OCR"
    )
    parser.add_argument(
        "--image",
        type=str,
        help="Path to single image file"
    )
    parser.add_argument(
        "--directory",
        type=str,
        help="Path to directory containing images"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file to save results (optional)"
    )
    parser.add_argument(
        "--language",
        type=str,
        default="eng",
        help="Tesseract language code (default: eng)"
    )
    parser.add_argument(
        "--preprocess",
        action="store_true",
        help="Apply image preprocessing before OCR"
    )
    parser.add_argument(
        "--recursive",
        action="store_true",
        help="Recursively process subdirectories"
    )

    args = parser.parse_args()

    # Process single image
    if args.image:
        try:
            text = extract_text_from_image(
                args.image,
                language=args.language,
                preprocess=args.preprocess
            )
            print("=== Extracted Text ===")
            print(text if text else "[No text detected]")
        except Exception as e:
            logger.error(f"Failed to process image: {str(e)}")
            exit(1)

    # Process directory
    elif args.directory:
        results = extract_text_from_directory(
            args.directory,
            output_file=args.output,
            language=args.language,
            recursive=args.recursive
        )
        if results:
            logger.info("Text extraction completed")
        else:
            logger.error("Failed to process directory")
            exit(1)

    else:
        parser.print_help()
        exit(1)
