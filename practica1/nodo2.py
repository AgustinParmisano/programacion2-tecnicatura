#!/usr/bin/python

class Node:

    def __init__(self,data,next):
        self.data=data
        self.next=next

    def last(self):
        act=self
        while act.next !=None:
            act=act.next
        return act

    def first(self):

        return self

    def len(self):
        act=self
        res=0
        while act.next !=None:
            res+=1
            act=act.next 
        res+=1
        return res

    def alldata(self):
        li=[]
        act=self
        while act.next !=None:
            li.append(act.data)
            act=act.next
        li.append(act.data)
        return li

    def sumatoria(self):
        act=self
        res=0
        while act.next !=None:
            res+=act.data
            act=act.next 
        res+=act.data
        return res

    def buscarDato(self,data):
        act=self
        while(act.next !=None)and(act.data !=data):
            act=act.next
        if act.data == data:
            return True
        return False

    def minDato(self):
        act=self
        min=9999
        while act.next !=None:
            if act.data < min:
                min=act.data
            act=act.next
        if act.data < min:
            min=act.data
        return min

    def maxDato(self):
        act=self
        max=-9999
        while act.next !=None:
            if act.data > max:
                max=act.data
            act=act.next
        if act.data > max:
            max=act.data
        return max

'''    def eliminarDato(self,data):
        act=self
        while (act.next !=None)and not(self.buscarDato(data)):
'''



n5 = Node(47,None)
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
