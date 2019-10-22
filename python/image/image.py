from PIL import Image, ImageFilter
import pytesseract


pytesseract.pytesseract.tessseract_cmd = 'C:/Users/lingkong/Downloads/tesseract-4.0.0-alpha/tesseract.exe'

text = pytesseract.image_to_string(Image.open('./NoC.JPG'))

#kitten = Image.open("NoC.JPG")
#blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
#blurryKitten.save("NoC_two.JPG")
#blurryKitten.show()

print(text)
