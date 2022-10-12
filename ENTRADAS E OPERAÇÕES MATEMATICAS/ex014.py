# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
# (0 °C × 9/5) + 32

celcius = float(input('Digite a temperatura em ºC: '))
f = (celcius * (9/5)+32)
print('A temperatura de {:.2f}ºC equivale a {:.2f} Fahrenheit'.format(celcius, f))