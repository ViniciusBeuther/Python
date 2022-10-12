# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual e o seu salario? R$ '))
print('O seu salário com 15% de aumento passou de R$ {:.2f} para R${:.2f}'.format(salario, (salario * 1.15)))
