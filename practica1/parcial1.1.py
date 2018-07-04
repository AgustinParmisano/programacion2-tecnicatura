#!/usr/bin/python

def niveluno(lista,num):
    if (num < 10):
        for i in lista:
            if (i%2 == 0):
                print(i/num)
            else:
                print(i*num)
        return True
    return False

lis=[20,15,30,40,9,7]
if niveluno(lis,20):
    print('ok')
else:
    print('no es de una cifra')
if niveluno(lis,5):
    print('ok')
else:
    print('no es de una cifra')
