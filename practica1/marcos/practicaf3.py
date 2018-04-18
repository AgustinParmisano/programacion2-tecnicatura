#!/usr/bin/python3

#El for va aca

        
for i in [10,35,"Hola","julia no vino",100,0]:
    try:
        div= 10/int(i)
        print("se puede dividir con %s"%(i))
        

    except ZeroDivisionError:

        print ("no se puede dividir con 0")

    except ValueError:
        print ("no es un caracter valido")

