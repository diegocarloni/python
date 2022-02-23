l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
p = l * a
t = p / 2
print('\nA parede tem {} m² \nÉ necessário {:.3f} litros de tinta para pintar essa parede'.format(p, t))
