lista = [2,4,0,2]

for i in lista:
	try:
		x = i / i
	except Exception as e1:
		print("no, bicho")
#		raise

try:
	valore = int("ATR")

except Exception as e2:
	print("Un str no es un int")
#	raise

try:
	print(lista[4])

except Exception as e3:
	print("No esta en la lista")
#	raise

lista2 = [0,1,2,3,"STR"]

def funcaono(lista,lista2):

	for i in lista:
		try:
			x=i/i
			print("[+]Resultado: {}".format(x))

			y = lista[3] / lista2[5]
			print(y)

			vauluee = lista[0] * int(lista2[4])
			print(valuee)

		except ZeroDivisionError:
			print("[-]No se puede dividir x 0")

		except ValueError:
			print("[-]un str no es un int")

		except IndexError:
			print("[-]El elemento solicitado no esta en la lista")

funcaono(lista,lista2)
