'''
Exercício 1 - Semana 3
Crie um programa que imprime todos 
os números pares no intervalo de 
0 a 20.
'''
pares = []
for c in range (1,20+1):
    if c % 2 == 0 :
        pares.append(c)
        print(c)
print(pares)