# Escreva um programa que converta metros para cm e mm
metros = float(input('Digite a medida que deseja converter em metros: '))
centimetros = metros * 100
milimetros = metros * 1000

print('O comprimento {:.2f} metro(s) é equivalente a {:.2f} centimetros e {:.2f} milimetros'.format(metros, centimetros, milimetros))