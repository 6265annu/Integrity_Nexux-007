import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

def ImgReader(ImageFile):
    config = r"--psm 6 --oem 3"
    img = Image.open(ImageFile)
    text = tess.image_to_string(img,config=config)
    print(text)
    if text == "":
        return "Please Provide an image with readable text."
    else:
        print(text)
        return text
