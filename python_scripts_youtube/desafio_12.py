p = float(input('Digite o preço do produto: R$ '))
d = p - (p*0.05)
print('\nO preço do produto é R$ {:.2f} em até 3x sem juros.\nSe você pagar o produto à vista, terá um desconto de 5%, então o preço será de: R$ {:.2f}'.format(p, d))
