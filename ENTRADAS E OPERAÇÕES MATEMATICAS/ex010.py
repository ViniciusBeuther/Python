saldo = float(input('Digite o seu saldo bancário: R$ '))
dolares = saldo / 5.29
print('Com R${:.2f} voce pode comprar U$ {:.2f}'.format(saldo, dolares))