#!/usr/bin/python3
def connect (ip, port):
    print (" [+] Trying to connect to {} for port {}".format(ip, port))
    return [ip, port]


myip = input ("ingrese una variable ip: ")
myport = input ("ingrese una variable port: ")

connect(myip, myport)


'''La variables por defecto, se definen junto con la funcion y salvo que se ingrese un valor diferente cuando se llama a la misma, toman ese valor
Sirven para que la funcion se ejecute a pesar de no recibir ningun parametro'''
'''Ejemplo: 
def saludo (nombre,mensaje='Hola'):
    print ("{}, {}".format(mensaje, nombre))

saludo('Andrea')
print''
saludo('Daniel', 'Adios')

 Teniendo como salida:

Hola, Andrea

Adios, Daniel'''
               

'''Existen dos tipos de argumentos en Python: los convencionales y aquellos que están sujetos a un nombre específico, generalmente identificados como args (arguments) y kwargs (keyword arguments), respectivamente.
Cuando en una función uno de sus argumentos lleva un valor por defecto, éste se convierte automáticamente en un keyword argument o argumento clave-valor'''

''' Ejemplo:     
def h(a, b=4, c=2):
    return a + b*c

h(1, c=10)
devuelve 41'''

'''Para que una función tome una cantidad indefinida de argumentos, se utiliza la expresión *args.

def f(*args):
    return args
                
f(1, 5, True, False, "Hello, world!")
devuelve (1, 5, True, False, 'Hello, world!')'''

'''De forma análoga funcionan los keyword arguments, que son representados con dos asteriscos (**) y el nombre kwargs. Cabe destacar que los nombres de estos parámetros son indiferentes; args y kwargs son utilizados simplemente por convención.

def f(**kwargs):
    return kwargs
                
f(a=1, b=True, h=50, z="Hello, world!")
devuelve{'a': 1, 'h': 50, 'b': True, 'z': 'Hello, world!'}'''

'''En este caso kwargs es un diccionario que contiene el nombre de cada uno de los argumentos junto con su valor. Siendo esto así, el orden de los mismos es indistinto.

Ambos métodos pueden ser implementados en una misma función como excepción al error de sintaxis.

def f(*args, **kwargs):
    return args, kwargs

args, kwargs = f(True, False, 3.5, message="Hello, world!", year=2014)
devuelve args(True, False, 3.5)
devuelve kwargs{'message': 'Hello, world!', 'year': 2014}'''

