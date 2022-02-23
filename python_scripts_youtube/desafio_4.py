a = input ('Digite algo: ')
print('O tipo primitivo desse valor é:', type(a))
print('O tipo primitivo desse valor é: {}'.format(type(a)))

print('Só tem espaços? ', a.isspace())
print('Só tem espaços? {}'.format(a.isspace()))

print('É um número? ', a.isnumeric())
print('É um número? {}'.format(a.isnumeric()))

print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minusculas? ', a.islower())
print('Está capitalizada? ', a.istitle())

