import os
from PIL import Image


for p,s,f in os.walk(r'C:\Users\marco\desktop\mestrado\fotosMarcacaoRenome'):
    for img in f:
        name = img.split('.JPG')
        img_rgb = Image.open(os.path.join(p,img))
        img_r = img_rgb.getchannel(0)
        img_new = Image.new('L', (img_rgb.size[0],img_rgb.size[1]),0)
        img_new.paste(img_r,(0,0))
        img_new.save(os.path.join(r'C:\Users\marco\desktop\mestrado/img_r',name[0]+' r.JPG'))
        img_g = img_rgb.getchannel(1)
        img_new = Image.new('L', (img_rgb.size[0],img_rgb.size[1]),0)
        img_new.paste(img_g,(0,0))
        img_new.save(os.path.join(r'C:\Users\marco\desktop\mestrado/img_g',name[0]+' g.JPG'))
        img_b = img_rgb.getchannel(2)
        img_new = Image.new('L', (img_rgb.size[0],img_rgb.size[1]),0)
        img_new.paste(img_b,(0,0))
        img_new.save(os.path.join(r'C:\Users\marco\desktop\mestrado/img_b',name[0]+' b.JPG'))
        
