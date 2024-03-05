'''
Exercício 3 - Semana 3
Crie um programa que lê do teclado
sucessivos números de matricula (int).
O programa deve parar de ler os números 
quando a matricula 0 for digitada.
Ao final deve apresentar os números de 
matriculas separados em 3 grupos.
'''
div = 1
g1 = [] ; g2 = [] ; g3 = []
while True :
    mat = int(input())
    if mat == 0 :
        break
    if div == 1 :
        g1.append(mat)
    if div == 2 :
        g2.append(mat)
    if div == 3 :
        g3.append(mat)
        div = 0
    div += 1
print(g1)
print(g2)
print(g3)