a = input ('Digite algo: ')
print('O tipo primitivo de {} é: {}'.format(a, type(a)))
print('{} Só tem espaços? {}'.format(a, a.isspace()))
print('{} É um número? {}'.format(a, a.isnumeric()))
print('{} É alfabetico? {}'.format (a, a.isalpha()))
print('{} É alfanumerico? {}'.format (a, a.isalnum()))
print('{} Está em maiúsculas? {}'.format(a, a.isupper()))
print('{} Está em minusculas? {}'.format (a, a.islower()))
print('{} Está capitalizada? {}'.format (a, a.istitle()))
