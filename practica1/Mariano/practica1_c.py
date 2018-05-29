lista = []

for i in(21, 80, 443, 25, 22, 8080):
	lista.append(i)

print(lista)

print(sorted(lista))

print("""El numero "80" esta en la posicion {}""".format(lista.index(80)))

del lista[lista.index(443)]
print(len(lista))

lista.insert(0, 8100)
#print(lista)
