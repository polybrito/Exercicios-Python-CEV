#Escreva um programa que leia um valor em metros, e exiba-o convertido em centímetros e milímetros
#1m=100cm
#1m=1000mm

metros=float(input('Digite a metragem: '))
print('{} em centímetros: {:.0f} \n{} em milímetros: {:.0f}'.format(metros, metros*100, metros, metros*1000))