cadena = "Esto es una concatenacion de caracteres"

cadena = cadena.upper()

print(cadena)

cadena = cadena.lower()

print(cadena)

cadena = cadena.replace('concatenacion de caracteres','cadena')

print(cadena)

print("""se ubicara la posicion de la palabra "una" en la cadena con .find()""")

print(cadena.find("una")) 

print("""la palabra "una" se encuentra en la posicion {} de la cadena. Se ubico con .index""".format(cadena.index("una")))
