import os
g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\R_teste_imagens.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\R_teste_imagens\190 200218 10fx sl pc embaixo r g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\R_teste_imagens'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\R_teste_imagens',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()


g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\G_teste_imagens.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\G_teste_imagens\190 200218 10fx sl pc embaixo g g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\G_teste_imagens'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\G_teste_imagens',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()


g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\B_teste_imagens.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\B_teste_imagens\190 200218 10fx sl pc embaixo b g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\B_teste_imagens'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\B_teste_imagens',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()









g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\R_treino_imagens.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\R_treino_imagens\1 070218 8fx sl pc embaixo r g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\R_treino_imagens'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\R_treino_imagens',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()


g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\G_treino_imagens.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\G_treino_imagens\1 070218 8fx sl pc embaixo g g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\G_treino_imagens'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\G_treino_imagens',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()


g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\B_treino_imagens.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\B_treino_imagens\1 070218 8fx sl pc embaixo b g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\B_treino_imagens'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\B_treino_imagens',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()

g.close()



g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\gray_treino_imagens.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\gray_treino_imagens\1 070218 8fx sl pc embaixo gray g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\gray_treino_imagens'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\gray_treino_imagens',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()







g = open(r'C:\Users\marco\OneDrive - usp.br\Área de Trabalho\Mestrado\Resultados\gray_teste_imagens.csv',"w+")
l = open(r'C:\Users\marco\desktop\mestrado\gray_teste_imagens\190 200218 10fx sl pc embaixo gray g0.csv',"r")
t = l.readlines()
count0 = 0
count1 = 0
count2 = 0
count3 = 0
l = 0
g.write(t[0])
for s,p,f in os.walk(r'C:\Users\marco\desktop\mestrado\gray_teste_imagens'):
    for k in f:
        file = open(os.path.join(r'C:\Users\marco\desktop\mestrado\gray_teste_imagens',k),'r')
        texto = file.readlines()
        g.write(texto[1])
        g.write('\n')           
        file.close()
g.close()