m = float(input('Digite um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print('{} metros é equivalente à {:.0f} cm e\n{} metros é equivalente à {:.0f} mm'.format(m, cm, m, mm))
print('\n{} metros é equivalente à {} km'.format(m, km))
print('{} metros é equivalente à {} hm'.format(m, hm))
print('{} metros é equivalente à {} dam'.format(m, dam))
print('{} metros é equivalente à {} dm'.format(m, dm))
print('{} metros é equivalente à {} cm'.format(m, cm))
print('{} metros é equivalente à {} mm'.format(m, mm))
