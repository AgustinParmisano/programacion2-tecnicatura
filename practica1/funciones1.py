#!/usr/bin/python3
def connect (ip, port):
    print (" [+] Trying to connect to {} for port {}".format(ip, port))
    return [ip, port]


myip = input ("ingrese una variable ip: ")
myport = input ("ingrese una variable port: ")

connect(myip, myport)


'''La variables por defecto, se definen junto con la funcion y salvo que se ingrese un valor diferente cuando se llama a la misma, toman ese valor'''
''' Sirven para que la funcion se ejecute a pesar de no recibir ningun parametro'''
'''Ejemplo: 
def saludo (nombre,mensaje='Hola'):
    print ("{}, {}".format(mensaje, nombre))

saludo('Andrea')
print''
saludo('Daniel', 'Adios')

 Teniendo como salida:

# ./prueba.py
Hola, Andrea

Adios, Daniel'''
               

'''Existen dos tipos de argumentos en Python: los convencionales y aquellos que están sujetos a un nombre específico, generalmente identificados como args (arguments) y kwargs (keyword arguments), respectivamente.
Cuando en una función uno de sus argumentos lleva un valor por defecto, éste se convierte automáticamente en un keyword argument o argumento clave-valor'''

''' Ejemplo:     
def h(a, b=4, c=2):
    return a + b*c

h(1, c=10)
devuelve 41'''

