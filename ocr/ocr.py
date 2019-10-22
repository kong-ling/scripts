from PIL import Image
import pytesseract
#text=pytesseract.image_to_string(Image.open('ocr.gif'), lang='chi_sim')
text=pytesseract.image_to_string(Image.open('ocr.gif'))
print(text)
