# Crie um programa que leia quanto dinheiro a pessoa tem na carteira, e mostre quantos dólares ela pode comprar
# US$1,00 = R$5,72

real = float(input('Quantos reais você tem? R$'))
dolar = real/5.72
print('-'*20)
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))