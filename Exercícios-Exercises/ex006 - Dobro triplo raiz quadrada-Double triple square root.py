#Crie um algoritmo que leia um número e mostre seu dobro, seu triplo e raiz quadrada

num1=int(input('Digite um número para descobrir seu dobro, triplo e raiz quadrada: '))
print('O dobro de {} é {}, o triplo é {}, e a raiz quadrada é {:.1f}'.format(num1, num1*2, num1*3, num1**(1/2)))

#num1**(1/2) também pode ser feito com pow(num1, (1/2)
