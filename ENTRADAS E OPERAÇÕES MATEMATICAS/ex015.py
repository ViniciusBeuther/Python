#  Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
#  quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

percorrido = float(input('Digite a distancia percorrida: '))
dias = int(input('Digite quantos dias voce alugou o carro: '))
conta = (60.0 * dias) + (percorrido * 0.15)
print('O valor total de {:.2f} km rodados por {:.2f} dia(s) foi de R$ {:.2f}'.format(percorrido, dias, conta))