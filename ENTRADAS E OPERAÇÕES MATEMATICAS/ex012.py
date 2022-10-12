# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor = float(input('Digite o preço do produto: R$ '))
print('O valor do produto (R$ {:.2f}) com 5% de desconto, agora custa apenas R$ {:.2f}'.format(valor, (valor*0.95)))
