# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados

largura = float(input('Digite a largura da parede que deseja pintar: '))
altura = float(input('Digite a altura da parede que deseja pintar: '))
area = largura * altura
print('A quantidade necessaria de tinta e de {:.2f} litros para pintar {:.2f} metros quadrados'.format((area/2), area))
