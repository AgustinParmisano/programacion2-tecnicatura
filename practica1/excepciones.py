#!/usr/bin/python3
#try:
#    10 / 0
#except Exception as ai:
#    print ("se produjo una excepcion")
#    raise

#division por cero, valor, fuera de rango

lista= [24, 56, 84, 12, 95]

elemento= input('seleccione un numero del 1 al 5: ')
divisor= input('ingrese un divisor: ')

try: 
    resultado= lista[elemento-1] / divisor
    print(resultado)
    print('[+] todo bien')
except Exception as e1:
    print('[-] todo mal')
    raise
try:
    i= int('a')
except Exception as e2:
    raise
