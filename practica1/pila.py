#!/usr/bin/python

class Pila:

    def __init__(self):
        self.data=[]

    def is_empty(self):
        return(len(self.data)<1)

    def pop(self):
        if not self.is_empty():
            return(self.data.pop())
        return False

    def push(self,elem):
        self.data.append(elem)
        return len(self.data)

    def top(self):
        if not self.is_empty():
            return self.data[-1]
        return false

    def __str__(self):
        return self.data

'''    def eliminarDato(self,data):
        act=self
        while (act.next !=None)and not(self.buscarDato(data)):
'''

pila1 = Pila()
pila2 = Pila()
pila1.push(5)
pila1.push(10)
pila2.push(2)
print(pila1.top()/pila2.top())



''' n5 = Node(47,None)
n4 = Node(75,n5)
n3 = Node(4,n4)
n2 = Node(33,n3)
n1 = Node(25,n2)
n0 = Node(23,n1)
print (n0.last().data)
print (str(n0.alldata()))
print (n0.minDato())
print (n0.maxDato())
print (n0.sumatoria())
print (n0.len())
print (n0.first().data)
print (n0.buscarDato(25))
print (n0.buscarDato(20))
'''
