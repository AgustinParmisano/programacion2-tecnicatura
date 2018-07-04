#!/usr/bin/python3

def nivel3(lista,num):
    for elem in lista:
        try:
            resul= elem/num
        except:
            resul= elem
        print(resul)

lis= ['casa',48,'hombre',84,65,'pez']
nivel3(lis,2)
