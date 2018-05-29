try:
	divcero = int(input("ingrese un numero que explotara al dividirlo por 0: "))
	divcero/0
except ZeroDivisionError:
	print("naaaaaa, no se puede")

