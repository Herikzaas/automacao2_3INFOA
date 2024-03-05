'''
Exercício 1:
 Crie um programa que lê dois número
 inteiros do teclado e após imprime 
 o maior números dentre eles.
'''

n1 , n2 = map(int,input().split())

if n1 > n2 :
    print(n1)
else :
    print(n2)