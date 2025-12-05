"""
Convert multiple image files to a single PDF document.

This module provides utilities to batch convert image files (PNG, JPG, JPEG)
into a single consolidated PDF file.

Features:
- Convert multiple image formats to PDF
- Batch processing support
- Configurable output directory
- Error handling for invalid images
- Logging support

Usage:
    python image2pdf.py --directory /path/to/images/ --output result.pdf
"""

import os
import logging
from pathlib import Path
from typing import List

import img2pdf

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def convert_images_to_pdf(
    image_directory: str,
    output_path: str = "output.pdf",
    image_formats: List[str] = None,
) -> bool:
    """
    Convert all images in a directory to a single PDF file.

    Args:
        image_directory: Path to directory containing images
        output_path: Path where PDF will be saved (default: output.pdf)
        image_formats: List of file extensions to process (default: ['png', 'jpg', 'jpeg'])

    Returns:
        bool: True if successful, False otherwise

    Raises:
        ValueError: If image_directory doesn't exist
        IOError: If PDF write operation fails
    """
    if image_formats is None:
        image_formats = ["png", "jpg", "jpeg"]

    # Validate input directory
    if not os.path.isdir(image_directory):
        raise ValueError(f"Image directory not found: {image_directory}")

    try:
        # Get all image files
        image_files = set()
        for fmt in image_formats:
            # Find files with lowercase extension
            for file_path in Path(image_directory).glob(f"*.{fmt}"):
                image_files.add(file_path)
            # Find files with uppercase extension
            for file_path in Path(image_directory).glob(f"*.{fmt.upper()}"):
                image_files.add(file_path)

        if not image_files:
            logger.warning(f"No images found in {image_directory}")
            return False

        logger.info(f"Found {len(image_files)} images to convert")

        # Convert images to PDF - sort by filename
        image_list = [str(img) for img in sorted(image_files)]

        # Ensure output directory exists
        output_file_path = Path(output_path)
        output_file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "wb") as pdf_file:
            pdf_file.write(img2pdf.convert(image_list))

        logger.info(f"PDF successfully created: {output_path}")
        return True

    except Exception as e:
        logger.error(f"Error converting images to PDF: {str(e)}")
        return False


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert images to PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert all images in current directory
  python image2pdf.py

  # Specify custom input and output directories
  python image2pdf.py --directory ./photos --output result.pdf

  # Convert images from specific directory
  python image2pdf.py --directory /path/to/images --output combined.pdf
        """,
    )
    parser.add_argument(
        "--directory",
        type=str,
        default=".",
        help="Directory containing images (default: current directory)",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output.pdf",
        help="Output PDF file path (default: output.pdf)",
    )

    args = parser.parse_args()

    try:
        success = convert_images_to_pdf(args.directory, args.output)
        exit(0 if success else 1)
    except ValueError as e:
        logger.error(f"Invalid input: {str(e)}")
        exit(1)
    except IOError as e:
        logger.error(f"File operation failed: {str(e)}")
        exit(1)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        exit(1)
