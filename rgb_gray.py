import os
from PIL import Image


for p,s,f in os.walk(r'C:\Users\marco\desktop\mestrado\fotosMarcacaoRenome'):
    for img in f:
        name = img.split('.JPG')
        img_rgb = Image.open(os.path.join(p,img))
        img_gray = img_rgb.convert('L')
        img_gray.save(os.path.join(r'C:\Users\marco\desktop/mestrado\img_gray',name[0]+' gray.JPG'))