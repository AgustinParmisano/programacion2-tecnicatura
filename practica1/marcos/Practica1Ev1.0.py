# funcion que detecta si el caracter pertenece a un elemento del alfabeto español o el CERO

def igual(e):
	alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',int(0),' ']
	salir = 0
	limite = len(alfabeto)
	limite2 = len(e)
	pos = 0
	pos2 = 0
	while salir == 0:
		if alfabeto[pos] == e[pos2]:
			return "incorrecto"
			salir = 1
		if limite-1 == pos:
			salir = 1
			return "correcto"
		pos = pos+1

exit = 0
while exit == 0:
	number = ""
	number = input("Ingrese Un Numero Terricola, para salir ingrese $: ")
	if number == "$":
		exit = 1
		continue
	if (igual(number)) == ("incorrecto"):
		print("Caracter incorrecto, Vuelva a intentarlo")
		continue
	if (igual(number)) == ("correcto"):
		number = int(number)
		numdivido = int(number/2)
		print (numdivido)
		resto = numdivido%2
		if isinstance(numdivido,int):
			if resto == 0:
				print ("La Division en 2 del numero %i es %i que es par"% (number,numdivido))
			else:
				print ("La Division en 2 del numero %i es %i que es impar"% (number,numdivido))
		else:
			print("el numero no es entero")
			print(numdivido)

