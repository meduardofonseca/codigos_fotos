import os
g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\R_teste.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\R_teste\190 200218 10fx sl pc embaixo r g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\R_teste'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\R_teste',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()


g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\G_teste.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\G_teste\190 200218 10fx sl pc embaixo g g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\G_teste'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\G_teste',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()


g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\B_teste.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\B_teste\190 200218 10fx sl pc embaixo b g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\B_teste'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\B_teste',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()









g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\R_treino.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\R_treino\1 070218 8fx sl pc embaixo r g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\R_treino'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\R_treino',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()


g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\G_treino.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\G_treino\1 070218 8fx sl pc embaixo g g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\G_treino'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\G_treino',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()


g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\B_treino.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\B_treino\1 070218 8fx sl pc embaixo b g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\B_treino'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\B_treino',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()

g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\gray_treino.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\gray_treino\1 070218 8fx sl pc embaixo gray g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\gray_treino'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\gray_treino',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()







g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\gray_teste.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\gray_teste\190 200218 10fx sl pc embaixo gray g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\gray_teste'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\gray_teste',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()