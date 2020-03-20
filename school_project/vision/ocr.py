from PIL import Image
import pytesseract
  
img = Image.open('test.jpeg')
text = pytesseract.image_to_string(img, lang='eng')
print(text)

'''
pip install pytesseract
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

'''
