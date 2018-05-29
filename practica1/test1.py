#!/usr/bin/python3

for i in range(-3,10):
	try:
		print("hola")

		print((20 / 10))

		print(str(10 / i))

		#print(variable)

		#print("hola" + 10)

		l = [1,2,3]

		#print(l[3])
	
		print("Esta es la i sin errores: {}".format(i))

	except Exception as e:
		print("Esta es la i con errores: {}".format(i))
		print("Hubo un error en el programa: {}".format(str(e)))

'''for i in range  (1,5):

	
 		try:
         		x = int(input("Ingrese un numero: "))
         		break
 		except ValueError:
        		 print("Jodete por no poner un numero, volve a intentarlo")
'''

for i in range  (1,5):

             
                try:
			
                        x = int(input("Ingrese un numero: "))
                        if x in range (1,5):
				print("yuj")
			else
				print("uhnuyh")
                except RuntimeError:
                         print("Jodete por no poner un numero, volve a intentarlo")
