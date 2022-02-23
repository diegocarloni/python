d = int(input('Informe quantos dias o veiculo foi alugado: '))
km = float(input('Informe quantos km rodados: '))
o = (d * 60) + (km * 0.15)
print('\nO preco total a pagar é R$ {:.2f}'.format(o))
