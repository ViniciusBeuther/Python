entrada = input('Digite algo aqui: ') # INPUT RESULTA SEMPRE EM STR
print('A variavel e do tipo: ', type(entrada))
print('Tem somente espaços? ', entrada.isspace()) # Valores antes do ponto são o objeto
print('E numerico: ', entrada.isnumeric())
print('É alfabetico: ', entrada.isalpha())
print('É maiusculo: ', entrada.isupper())
print('É minusculo: ', entrada.islower())
print('É capitalizado: ', entrada.istitle())
