#!/usr/bin/python

def niveldos(lista,num):
    lis=[]
    for pal in lista:
        if (len(pal) == num):
            lis.append(pal)
    return(lis)

lis1=['pepe','pedro','jose','esteban','juan']
lis2=['perro','gato','raton','vaca','toro','burro']

print(niveldos(lis1,4))
print(niveldos(lis1,5))
print(niveldos(lis1,7))
print(niveldos(lis2,4))
print(niveldos(lis2,5))
print(niveldos(lis2,7))
