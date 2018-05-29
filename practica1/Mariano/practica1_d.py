servicios = {'ftp':21,'ssh':22,'smtp':25,'http':80,'http-alt?':8080,'?':8100}

print(sorted(servicios.keys()))

print(servicios.items())


if 'ftp' in servicios != False:
	print("""el diccionario tiene la clave "ftp" y su valor es {}""".format(servicios['ftp']))

#no se porque el if me funciona con != False y no lo hace con == True o = True

print('ftp' in servicios)

for key in servicios:
	print("[+] Found vulnerabilities with {} on port {}".format(key, servicios[key]))
