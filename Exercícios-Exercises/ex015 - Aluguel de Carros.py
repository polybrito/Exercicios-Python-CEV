#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de  dias pelos quais ele foi alugado. Calcule o preço a pagar. 
#Valor dia = R$60
#Valor km = R$0,15

dia = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos km você percorreu com o carro? '))

pagamento = (dia*60 + km*0.15)

print('Você deve pagar RS{:.2f}'.format(pagamento))