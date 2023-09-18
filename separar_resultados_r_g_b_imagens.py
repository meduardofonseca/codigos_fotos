import os
import re
import shutil
r = ' r '
g =' g '
b = ' b '

for p,s,f in os.walk(r'C:\Users\marco\Desktop\mestrado\Resultados_linha_rgb_imagens'):
    for img in f:
        
        
        if re.search(r,img,re.IGNORECASE):
           shutil.copy(os.path.join(r'C:\Users\marco\Desktop\mestrado\Resultados_linha_rgb_imagens',img),r'C:\Users\marco\Desktop\mestrado\resultados_r_imagens')
        if re.search(g,img,re.IGNORECASE):
           shutil.copy(os.path.join(r'C:\Users\marco\Desktop\mestrado\Resultados_linha_rgb_imagens',img),r'C:\Users\marco\Desktop\mestrado\resultados_g_imagens')
        if re.search(b,img,re.IGNORECASE):
           shutil.copy(os.path.join(r'C:\Users\marco\Desktop\mestrado\Resultados_linha_rgb_imagens',img),r'C:\Users\marco\Desktop\mestrado\resultados_b_imagens')
         
           
for p,s,f in os.walk(r'C:\Users\marco\Desktop\mestrado\Resultados_linha_rgb'):
    for img in f:
        
        
        if re.search(r,img,re.IGNORECASE):
           shutil.copy(os.path.join(r'C:\Users\marco\Desktop\mestrado\Resultados_linha_rgb',img),r'C:\Users\marco\Desktop\mestrado\resultados_r')
        if re.search(g,img,re.IGNORECASE):
           shutil.copy(os.path.join(r'C:\Users\marco\Desktop\mestrado\Resultados_linha_rgb',img),r'C:\Users\marco\Desktop\mestrado\resultados_g')
        if re.search(b,img,re.IGNORECASE):
           shutil.copy(os.path.join(r'C:\Users\marco\Desktop\mestrado\Resultados_linha_rgb',img),r'C:\Users\marco\Desktop\mestrado\resultados_b')