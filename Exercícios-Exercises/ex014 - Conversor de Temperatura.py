#Escreva um programa que converta uma temperatura em °C para °F

#A diferença entre os pontos de congelamento e ebulição da água nas duas escalas é:
#Em Celsius: 100°C (de 0°C a 100°C).
#Em Fahrenheit: 180°F (de 32°F a 212°F).

#Então, para ir de C para F, é preciso:
#Ajustar a escala: multiplicar (c*9/5), ou (c*9/5)), ou (c*1.8)
#Ajusta o ponto de partida: dicionar 32

c = float (input('Coloque o valor em °C:'))
f = c*9/5+32
print('A temperatua {}°C corresponde a {}°F.'.format(c, f))