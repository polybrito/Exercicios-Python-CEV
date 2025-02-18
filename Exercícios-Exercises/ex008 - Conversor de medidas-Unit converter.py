#Escreva um programa que leia um valor em metros, e exiba-o convertido em quilômetros, hectômetros, decâmetros, decímetros, centímetros e milímetros

#1m=10dc
#1m=100cm
#1m=1000mm

m = float(input('Digite a metragem: '))

km= m/1000
hm= m/100
dam= m/10
dm= m*10
cm = m*100
mm= m*1000

print('-'*20)
print('Tabela de medidas baseada em {}m:'.format(m))
print('{}m = {}km \n{}m = {}hm \n{}m = {}dam \n{}m = {}dm \n{}m = {}cm \n{}m = {}mm'.format(m,km, m, hm, m, dam, m, dm, m, cm, m, mm))
