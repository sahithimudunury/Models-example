import pytesseract
from PIL import Image
import os
img_path = r'C:\Users\Dell\Pictures\Screenshots\Screenshot 2026-03-10 100334.png'
if not os.path.exists(img_path):
    print('Image path not found')
else:
    try:
        text = pytesseract.image_to_string(Image.open(img_path))
        print('OCR Output:')
        print(text)
    except Exception as e:
        print('Error', e)
