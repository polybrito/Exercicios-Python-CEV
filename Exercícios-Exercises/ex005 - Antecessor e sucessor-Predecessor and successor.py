#Faça um programa que leia um número inteiro e mostre na tela seu sucessor e antecessor

n1=int(input('Digite um valor para descobrir seu sucessor e seu antecessor: '))
print('O sucessor de {} é {}, e o antecessor é {}.'.format(n1, n1+1, n1-1))