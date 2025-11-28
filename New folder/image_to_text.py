import pytesseract


from PIL import Image


# Path to Tesseract executable (change this to your Tesseract installation path)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_text_from_image(image_path):
    try:
        # Open the image using PIL (Python Imaging Library)
        image = Image.open(image_path)
        # Use pytesseract to perform OCR on the image
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    # Replace with your image file path
    image_path = "D:\Data Structure Code\Automation\image3.jpeg"

    extracted_text = extract_text_from_image(image_path)

    if extracted_text:
        print("Extracted Text:")
        print(extracted_text)
    else:
        print("Text extraction failed.")
