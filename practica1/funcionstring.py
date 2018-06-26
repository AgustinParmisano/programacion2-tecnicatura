#!/usr/bin/python

def funstring(cadena,nro):
    lis=[]
    for i in range(0,len(cadena),nro):
        lis.insert(0,cadena[i:i+nro])
    print(''.join(lis))


funstring('Este es otro ejemplo!',5)



'''
    largo=len(cadena)
    i=0
    j=nro-1
    while largo > 0:
        if largo >= j
            lis.append(cadena[i:j])
            j+=nro
        else
            lis.append(cadena[i:largo])
'''
