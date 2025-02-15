# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

valor = float(input('Qual o valor do produto? '))
desconto = 5/100*valor
novo_valor = valor-desconto

print('O valor do desconto será {}, e o novo valor do produto será {}.'.format(desconto, novo_valor))
